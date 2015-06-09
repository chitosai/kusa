import json
from config import *

def init():
	# put the default config file
	# and check if current dir is alreay inited
	try:
		f = open(CONFIG_FILE_NAME, 'r')
		print 'You have already initialized Chitose Blog in this dir'
		return False
	except:
		f = open(CONFIG_FILE_NAME, 'w')
		f.write(DEFAULT_CONFIG)
	finally:
		f.close()

	# make dir
	for dir_name in PRESERVED_DIRS:
		new_dir = os.path.join(BASE_DIR, PRESERVED_DIR_PREFIX + dir_name)
		try:
			os.mkdir(new_dir)
		except:
			print 'Fail to create %s, path already exists?' % str(new_dir)