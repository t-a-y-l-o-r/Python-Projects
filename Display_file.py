'''
This script will read any file passsed to is and is inteded for 
shelve databases and txt files
'''

import sys
import re 
# import pprint
import shelve

dot_regex = re.compile(r'\.')

if len(sys.argv) == 2:
	# open the file and store the file name
	file = open(sys.argv[1],'r')
	file_str = sys.argv[1]
	file_type = ''
	file_index = 0

	# find the file type
	for position in re.finditer(dot_regex, file_str):
		file_index = position.start(0)
		file_type = file_str[file_index: ]

	if file_type == '.db':
		file_str = file_str[:file_index]
		file = shelve.open(file_str)
		keys = list(file.keys())

		for key in keys:
			print('Key:' + str(key) + '\n' + str(file[key]))
	else:
		print(file.read())

		

else:
	print('Display_file.py <file_name> - print contents of file.')
	print('This script should only be used with shelve databases and txt files.')