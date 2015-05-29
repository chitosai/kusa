import os, json
import config

def init():
	# put the default config file
	# and check if current dir is alreay inited
	try:
		f = open(config.config_file, 'r')
		print 'You have already initialized Chitose Blog in this dir'
		return False
	except:
		f = open(config.config_file, 'w')
		f.write(config.default_config)
	finally:
		f.close()

	# make dir
	cur_dir = os.path.abspath('.')
	for dir_name in config.dirs:
		new_dir = os.path.join(cur_dir, config.dir_prefix + dir_name)
		try:
			os.mkdir(new_dir)
		except:
			print 'Fail to create %s, path already exists?' % str(new_dir)