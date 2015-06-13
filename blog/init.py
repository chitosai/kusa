import json, pkgutil, os
from config import *

def init():
	# check if current dir is alreay inited
	if os.path.exists(CONFIG_FILE_NAME):
		print 'You have already initialized Chitose Blog in this dir'
		return False
	
	# make dir
	for dir_name in PRESERVED_DIRS:
		new_dir = os.path.join(BASE_DIR, PRESERVED_DIR_PREFIX + dir_name)
		try:
			os.mkdir(new_dir)
		except:
			print 'Fail to create %s, path already exists?' % str(new_dir)

	# put example files
	for file_path in EXAMPLE_FILES:
		example_file = pkgutil.get_data('blog', os.path.join('example', file_path))

		# make path for it
		file_dir = os.path.abspath(os.path.dirname(file_path))
		if not os.path.exists(file_dir):
			os.makedirs(file_dir)

		# write file
		f = open(file_path, 'w')
		f.write(example_file)
		f.close()