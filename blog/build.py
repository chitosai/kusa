import re, datetime
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

def get_post_name(file_name):
	'''Method to parse a string to date-permalink.ext array
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
	return post_config, post_content

def get_posts():
	'''Call this method to get posts from _post dir'''
	posts = []
	post_dir = os.path.join(BASE_DIR, PRESERVED_DIR_PREFIX + 'posts')
	for file_name in os.listdir(post_dir):
		post = {}
		# get permalink/date from file name
		post['permalink'], post['date'] = get_post_name(file_name)
		if not post['permalink']:
			print 'Fail to parse the file_name of "%s"' % file_name
			continue

		# then parse the content of the post file
		file_path = os.path.join(post_dir, file_name)
		post_config, post_content = get_post_content(file_path)
		if not post_config:
			print 'Failed to parse the config part of "%s"' % file_name
			continue

		# fill into the post dict
		post.update(post_config)
		post['content'] = post_content.decode('utf-8') # I don't know why but if I don't decode it jinja2 will raise an error

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

def build():
	# get user's config
	site = {}
	config = get_user_config()
	site.update(config)

	# traversal the _post dir to parse all the .markdown posts
	site['posts'] = get_posts()

	# traversal the _templates dir and get all templates
	templates = get_templates()

	# render the posts!
	template_env = jinja2.Environment(loader = jinja2.FileSystemLoader([PRESERVED_DIR_PREFIX + 'templates',
																		PRESERVED_DIR_PREFIX + 'includes']))
	for post in site['posts']:
		# process the permalink url
		file_name = site['permalink'] \
				 .replace(':title', post['permalink']) \
				 .replace(':date', post['date'].strftime('%Y-%m-%d')) \
				 .replace(':year', str(post['date'].year)) \
				 .replace(':month', str(post['date'].month)) \
				 .replace(':day', str(post['date'].day))
		# make sure file_name isn't started with /
		if file_name[0] == '/': 
			file_name = file_name[1:]

		# seperate file_name to array
		file_name_array = file_name.split('/')
		current_path = OUTPUT_DIR
		# and mkdir for it
		if len(file_name_array) > 1:
			for path in file_name_array:
				# if path contains empty part(//), just ignore it
				if path == '': continue
				current_path = os.path.join(current_path, path)
				try:
					os.mkdir(current_path)
				except:
					pass

		# render the post
		template = template_env.get_template(post['layout'] + '.html')
		content = template.render(site = site, page = post, content = post['content'], comments = site['comments'])

		# write to output file
		file_name = os.path.join(current_path, 'index.html')
		f = open(file_name, 'w')
		f.write(content.encode('utf-8'))
		f.close()

	# step.2 - traversal the root path and copy & compile all the .html pages



	# step.3 - just copy the whole _static dir to _dist: 1
