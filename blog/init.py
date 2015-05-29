import os

dirs = []

def init():
	# check if current dir is alreay inited
	try:
		f = open('.CHITOSE_INIT_FLAG', 'r')
		f.close()
		print 'You have already initialized Chitose Blog in this dir'
	except:
		f = open('.CHITOSE_INIT_FLAG', 'wb')
		return False

	# make dir

