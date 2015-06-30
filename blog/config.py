import os

# prefix to distinguish Kusa's preserved dir from user's own dir
PRESERVED_DIR_PREFIX = '_'

# dirs that will be created
PRESERVED_DIRS = ['posts', 'templates', 'static', 'dist', 'includes', 'data']

# config file name
CONFIG_FILE_NAME = '_config.yml'

# example files that should be put into user's blog folder
EXAMPLE_FILES = [
	'_config.yml',
	'index.markdown',
	'link/index.markdown',
	'feed/index.xml',
	'_static/main.css',
	'_data/links.yml',
	'_templates/base.html',
	'_templates/json.html',
	'_templates/post.html',
	'_posts/2015-06-14-hello-world.markdown',
	'_includes/comments.html'
]

# current path
BASE_DIR = os.path.abspath('.')
DATA_DIR = os.path.join(BASE_DIR, PRESERVED_DIR_PREFIX + 'data')
POST_DIR = os.path.join(BASE_DIR, PRESERVED_DIR_PREFIX + 'posts')
TEMPLATE_DIR = os.path.join(BASE_DIR, PRESERVED_DIR_PREFIX + 'templates')
OUTPUT_DIR = os.path.join(BASE_DIR, PRESERVED_DIR_PREFIX + 'dist')
STATIC_DIR = os.path.join(OUTPUT_DIR, 'static')