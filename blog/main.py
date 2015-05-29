#!/usr/bin/env python

import sys
from init import *

def build():
	print 'build'

action = {
	'build' : build,
	'init'  : init
}
def main():
	# check input
	try:
		act = sys.argv[1]
	except:
		exit('No input')

	if act not in action :
		exit('Unknown input')

	# do
	action.get(act)();

if __name__ == '__main__':
	main()