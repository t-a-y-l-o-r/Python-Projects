# Walking_dir.py - Walks the passed dir and all of it's subfolders 

import os
import sys

user_dir = ''

if len(sys.argv) == 2:
	user_dir = sys.argv[1]
else:
	print('Walking_dir.py <dir> - Walks the dir top-down.')


for folder_name, subfolders, filnames in os.walk(user_dir):
	print('The current folder is: ' + folder_name)

	for subfolder in subfolders:
		print('SUBFOLDER OF ' + folder_name + ': ' + subfolder)

	for filename in filnames:
		print('FILE INSIDE ' + folder_name + ': ' + filename)
		