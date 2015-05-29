import os, json

# dirs that will be created
dirs = ['posts', 'templates', 'static']

# default config file
default_config = '''{
	"url"         : "http://yourdomain/",
	"name"        : "your blog name",
	"description" : "whatever you like",
	"author"      : "your name",
	"feed"        : "something like /feed"
}'''

def init():
	global dirs, default_config

	# put the default config file
	# and check if current dir is alreay inited
	try:
		f = open('config.json', 'r')
		print 'You have already initialized Chitose Blog in this dir'
		return False
	except:
		f = open('config.json', 'w')
		f.write(default_config)
	finally:
		f.close()

	# make dir
	cur_dir = os.path.abspath('.')
	for dir_name in dirs:
		new_dir = os.path.join(cur_dir, dir_name)
		try:
			os.mkdir(new_dir)
		except:
			print 'Fail to create %s, path already exists?' % str(new_dir)