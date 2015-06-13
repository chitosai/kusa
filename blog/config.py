import os

# prefix to distinguish chitose's preserved dir from user's own dir
PRESERVED_DIR_PREFIX = '_'

# dirs that will be created
PRESERVED_DIRS = ['posts', 'templates', 'static', 'dist', 'includes', 'data']

# config file name
CONFIG_FILE_NAME = '_config.yml'

# default config file
DEFAULT_CONFIG = '''\
url: http://youblogdomain/
name: your blog name
description: anything you like
author: the default author
permalink: /:year/:month/:title
rss_path: /feed
comments: true
'''

# current path
BASE_DIR = os.path.abspath('.')
DATA_DIR = os.path.join(BASE_DIR, PRESERVED_DIR_PREFIX + 'data')
POST_DIR = os.path.join(BASE_DIR, PRESERVED_DIR_PREFIX + 'posts')
TEMPLATE_DIR = os.path.join(BASE_DIR, PRESERVED_DIR_PREFIX + 'templates')
OUTPUT_DIR = os.path.join(BASE_DIR, PRESERVED_DIR_PREFIX + 'dist')
STATIC_DIR = os.path.join(OUTPUT_DIR, 'static')