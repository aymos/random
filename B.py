#!/usr/bin/python

#---colors---
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

## -- main -- 
import os,sys,time

#error handling ------------------------
if len(sys.argv) < 2:
	sys.stderr.write('ERROR - Specify the path\n')
	sys.exit(1)
filename=os.path.abspath(sys.argv[1])
if not os.path.exists(sys.argv[1]):
	sys.stderr.write('ERROR - Invalid path\n')
	sys.exit(1)
#filename=os.path.abspath(sys.argv[1])
if not os.access(filename,os.R_OK):
	if not os.access(filename,os.X_OK):
		sys.stderr.write('ERROR - Not permitted\n')
		sys.exit(1)

# valid path

x=len(filename.split('/'))

for root, dir, files in os.walk(filename):
    path = root.split('/')
   
    print ' |'+bcolors.OKBLUE+'\033[1m' + (len(path) - 1-x) *'    '+' |#--------    Folder Name : ' , os.path.basename(root) + '/    --------#' +'\033[0m'+bcolors.ENDC
    if os.listdir(os.path.abspath(root)) == []:
	    print ' |'+bcolors.FAIL+"                            [EMPTY FOLDER]"+bcolors.ENDC
	    print ' |'

    for file in files:
	if files == []:
		print 'empty'
	statinfo=os.stat(root+'/'+file)
	print  ' |'+(len(path)-x)*'    '+' |'
        print  ' |'+(len(path)-x)*'    '+' #-', file 
	print ' |'+bcolors.OKGREEN+ (len(path)-x)*'    '+' | Last modified:%s' %time.ctime(os.path.getmtime(root+'/'+file)),
	print '   Size: ',statinfo.st_size,' Bytes '+bcolors.ENDC
		
