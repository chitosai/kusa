import os, re, datetime
import jinja2
from config import *

def parse_post_file_name(file_name):
	'''Method to parse a string to date-permalink.ext array
	   example: 2015-05-21-wtf-email-format.markdown'''
	m = re.search('^(\d{4})-(\d{2})-(\d{2})-(.+?)\.markdown$', file_name)
	if m:
		date = datetime.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
		return m.group(4), date
	else:
		print 'Fail to parse the file_name of "%s"' % file_name
		return False, False

def build():
	# step.1 - traversal the _post dir to compile all the .md posts
	post_list = {}
	cur_dir = os.path.join(os.path.abspath('.'), PRESERVED_DIR_PREFIX + 'posts')
	for p in os.listdir(cur_dir):
		post = {}
		# get permalink/date from file name
		post['permalink'], post['date'] = parse_post_file_name(p)
		if not post['permalink']:
			continue
			
		# do next staffs 
			
	# step.2 - traversal the root path and copy & compile all the .html pages

	# step.3 - just copy the whole _static dir to _dist: 1