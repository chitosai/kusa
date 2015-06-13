# -*- coding: utf-8 -*-
import re, datetime, shutil
import jinja2, yaml, mistune
from config import *

def get_user_config():
	'''Read user's config'''
	f = open(CONFIG_FILE_NAME, 'r')
	try:
		config = yaml.load(f.read())
		# pre-process config
		if 'url' not in config or 'name' not in config or 'permalink' not in config \
		    or 'author' not in config:
		    exit('Make sure you have url/name/author/permalink in your config file!')
	except:
		config = {}
	finally:
		f.close()
		return config

def get_pages(path):
	'''Get all the pages under chitose root dir'''
	files = os.listdir(path)
	pages = []
	for file_name in files:
		# check if the file is preserved by chitose or hidden in os
		if file_name[0] in [PRESERVED_DIR_PREFIX, '.']:
			continue

		# get relpath
		file_rel = os.path.relpath(os.path.join(path, file_name))

		# if dir, iter it on
		if os.path.isdir(file_rel):
			pages.extend(get_pages(file_rel))
			continue

		# is file? check its extension
		if os.path.splitext(file_name)[-1] in ['.html', '.xml', '.markdown']:
			# read its content
			page = {}
			page['file_path'] = file_rel
			page['permalink'] = os.path.dirname(file_rel)
			config, content = get_post_content(file_rel)
			if not config:
				print 'Failed to parse the config part of "%s"' % file_name
				continue

			page.update(config)
			page['content'] = content
			pages.append(page)

	return pages

def get_post_name(file_name):
	'''Method to parse a string to date-title.ext array
	   example: 2015-05-21-wtf-email-format.markdown'''
	m = re.search('^(\d{4})-(\d{2})-(\d{2})-(.+?)\.markdown$', file_name)
	if m:
		date = datetime.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
		return m.group(4), date
	else:
		return False, False

def get_post_content(file_path):
	'''Method to get the config & content of a post file'''
	# read file content
	f = open(file_path, 'r')
	file_raw = f.readlines()
	f.close()

	# check the first line
	if file_raw[0] != '---\n':
		return False, False

	# read the config part
	i = 1
	total = len(file_raw)
	while file_raw[i] != '---\n' and i < total:
		i += 1
	config_raw = ''.join(file_raw[1:i])

	# parse it using PyYAML
	try:
		post_config = yaml.load(config_raw)
	except:
		return False, False

	# get the content and compile markdown
	post_content_raw = ''.join(file_raw[i+1:])
	post_content = mistune.markdown(post_content_raw)

	# return the two parts
	return post_config, post_content.decode('utf-8') # I don't know why but if I don't decode it jinja2 will raise an error

def get_posts():
	'''Call this method to get posts from _posts dir'''
	posts = []
	for file_name in os.listdir(POST_DIR):
		post = {}
		# get title_en/date from file name
		post['title_en'], post['date'] = get_post_name(file_name)
		if not post['title_en']:
			print 'Fail to parse the file_name of "%s"' % file_name
			continue

		# then parse the content of the post file
		file_path = os.path.join(POST_DIR, file_name)
		post_config, post_content = get_post_content(file_path)
		if not post_config:
			print 'Failed to parse the config part of "%s"' % file_name
			continue

		# fill into the post dict
		post.update(post_config)
		post['content'] = post_content

		# append to posts
		posts.append(post)

	return posts

def get_templates():
	'''Parse all the template files in _templates dir and return a list'''
	templates = {}
	template_dir = os.path.join(BASE_DIR, PRESERVED_DIR_PREFIX + 'templates')
	# traversal the _templates dir
	for file_name in os.listdir(template_dir):
		# get the template name
		template_name = file_name.replace('.html', '')

		# read template content
		file_path = os.path.join(template_dir, file_name)
		f = open(file_path, 'r')
		template_content = ''.join(f.readlines())
		f.close()

		# append to templates
		templates[template_name] = template_content

	return templates

def render(site, page, template_env):
	# priority: post['permalink'] > site['permalink']
	if 'permalink' in page:
		permalink = page['permalink']
	else:
		permalink = site['permalink']
			 
	# make sure permalink isn't started with /
	if len(permalink) > 0 and permalink[0] == '/': 
		permalink = permalink[1:]

	# process the permalink
	if ':title' in permalink:
		permalink = permalink.replace(':title', page['title_en'])
	if ':date' in permalink:
		permalink = permalink.replace(':date', page['date'].strftime('%Y-%m-%d'))
	if ':year' in permalink:
		permalink = permalink.replace(':year', str(page['date'].year))
	if ':month' in permalink:
		permalink = permalink.replace(':month', str(page['date'].month))
	if ':day' in permalink:
		permalink = permalink.replace(':day', str(page['date'].day))

	# generate its url
	page['url'] = permalink

	# make path
	permalink = os.path.join(OUTPUT_DIR, permalink)
	try:
		os.makedirs(permalink)
	except:
		pass

	# call jinja2 to render the page content
	template = template_env.from_string(page['content'])
	page['content'] = template.render(site = site, page = page, comments = site['comments'])

	# call jinja2 again to fill the rendered content into templates
	if 'layout' in page and page['layout'] != 'none':
		template = template_env.get_template(page['layout'] + '.html')
		content = template.render(site = site, page = page, comments = site['comments'])
	else:
		content = page['content']

	# write to output file
	output_file = os.path.join(permalink, 'index.html')
	f = open(output_file, 'w')
	f.write(content.encode('utf-8'))
	f.close()

def copy_static():
	# first remove the current exist static dir
	if os.path.exists(STATIC_DIR):
		shutil.rmtree(STATIC_DIR)

	# and let shutil do the move staff
	shutil.copytree(os.path.join(BASE_DIR, PRESERVED_DIR_PREFIX + 'static'), STATIC_DIR)

def build():
	site = {}

	# get user's config
	config = get_user_config()
	site.update(config)

	# user's custom data
	site['data'] = {}

	# traversal the _post dir to parse all the .markdown posts
	site['posts'] = get_posts()

	# traversal the _templates dir and get all templates
	templates = get_templates()

	# render the posts!
	template_env = jinja2.Environment(loader = jinja2.FileSystemLoader([PRESERVED_DIR_PREFIX + 'templates',
																		PRESERVED_DIR_PREFIX + 'includes']))
	for post in site['posts']:
		render(site, post, template_env)

	# traversal the root path and copy & compile all the .html/.xml pages
	pages = get_pages('.')
	
	# render the pages
	for page in pages:
		render(site, page, template_env)

	# last, just copy the whole _static dir to _dist: 1
	copy_static()
