# prefix to distinguish chitose's preserved dir from user's own dir
PRESERVED_DIR_PREFIX = '_'

# dirs that will be created
PRESERVED_DIRS = ['posts', 'templates', 'static', 'dist']

# config file name
CONFIG_FILE_NAME = '_config.yml'

# default config file
DEFAULT_CONFIG = '''\
url: http://youblogdomain/
name: your blog name
description: anything you like
author: the default author
permalink: /w/:title
feed: /feed
comments: true
'''
