import os, re, datetime
import jinja2, yaml
from config import *

def parse_post_file_name(file_name):
	'''Method to parse a string to date-permalink.ext array
	   example: 2015-05-21-wtf-email-format.markdown'''
	m = re.search('^(\d{4})-(\d{2})-(\d{2})-(.+?)\.markdown$', file_name)
	if m:
		date = datetime.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
		return m.group(4), date
	else:
		return False, False

def parse_post_config(file_path):
	'''Method to parse the config part of a post'''
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

	# return the two parts
	post_content = ''.join(file_raw[i+1:])
	return post_config, post_content

def build():
	# step.1 - traversal the _post dir to compile all the .markdown posts
	post_list = {}
	post_dir = os.path.join(os.path.abspath('.'), PRESERVED_DIR_PREFIX + 'posts')
	for file_name in os.listdir(post_dir):
		post = {}
		# get permalink/date from file name
		post['permalink'], post['date'] = parse_post_file_name(file_name)
		if not post['permalink']:
			print 'Fail to parse the file_name of "%s"' % file_name
			continue

		# then parse the content of the post file
		file_path = os.path.join(post_dir, file_name)
		post_config, post_content = parse_post_config(file_path)
		if not post_config:
			print 'Failed to parse the config part of "%s"' % file_name
			continue

		# fill into the post dict
		post.update(post_config)
		post['content'] = post_content
			
	# step.2 - traversal the root path and copy & compile all the .html pages


	# step.3 - just copy the whole _static dir to _dist: 1