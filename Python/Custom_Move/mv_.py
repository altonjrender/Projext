#!/usr/bin/env python
import sys
import os
import platform
from shutil import copyfile
#Enables you to move a program file anywhere from source directory 
# You dont have to know OS commands just move/ change_dest/
#if help is requested interactive mode occurs
#have it execute from anywhere using the python command

list_files = []
profile_ = sys.argv[0];
dest = "C:\\Users\\reeves\\python\\TODOL\\"
curdir = str(os.path.dirname(os.path.abspath(__file__)))
##def format_file_out(list_files):

#check for the source file argument vaule to be non-empty
#DONT allow someone to overwrite this file
#DONT allow to overwrite a file with same name/directory
def check_args():
	try:
		sys.argv[1]
	except:
		print(":Check for source arguments!!")
		exit(1)

check_args()
	
##Was able to print out main.py for the list
##allow user to change 
##
##
##
for args in sys.argv:
	if(args!= profile_):
		#append files to list		
		l = str(args)
		list_files.append(l)
	print(list_files)
def dest_syntax():
	for fls in list_files:
		if(platform.system()=="Windows"):
			sender = curdir +"\\"
			print('\n')
			print("Moving File: ",fls)
			src = curdir+fls
			print("Source:  ",src)
			print(dest)

		else:
			cudir+="/"

	

#copyfile(filename1, "C:\Users\reeves\python\TODOL\")