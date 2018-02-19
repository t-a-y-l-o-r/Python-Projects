# Regex_search.py - Searches all files in the cwd for the passed regex expression
# python3 Regex_search.py <regex> - Searches the cwd for the argument regex 



import sys
import os
import re
from os import walk
import shelve

mypath = os.getcwd()
dir_regex = re.compile(r'/Users\w*\s*')


def open_cwd(user_regex, down=True):
	'''
	Walks the cwd and saves a list of all the filenames.
	By defualt and if true, down indicates the walk will
	continue top down for the entire tree.

	If false, down prevents the walk from continuing beyond the 
	cwd.
	'''
	f = []
	d = []
	valid_file_paths = []
	# by default searches the cwd and below (top-down)
	if down:
		for (dirpath, dirname, filename) in walk(mypath):
			f.extend(filename)
			d.append(dirpath)
	# otherwise will only search the cwd
	else:
		for (dirpath, dirname, filename) in walk(mypath):
			f.extend(filename)
			d.append(dirpath)
			break
	# cross refrence each file with each dirpath and save all 
	# valid combinations
	for directory in d:
		for file in f:
			if os.path.isfile(directory + '/'+  file) and (file != '.DS_Store'):
				valid_file_paths.append(directory + '/' + file)
	#open each file
	for file_path in valid_file_paths:
		file = open(file_path, 'r')
		# print(file)
		files_with_matches = []
		
		search_file(user_regex, file)
		file.close()
		


def search_file(user_regex, file):
	'''
	The purpose of this function is to search the passed file 
	for any matching expression as the passed expression.
	In the event that a match is found the file, line, and expression
	are all stored in a shelve file named: 'expressions_found.db'
	'''
	# catches any decoding errors
	try:
		# for storage later
		shelf_expression_found = shelve.open('expressions_found')

		# grab each indivudual line 
		for line in file.readlines():
			# the user determins which experssion to search for 
			if not isinstance(user_regex, str):
				user_regex = str(user_regex)
			regex_to_use = re.compile(r'' + re.escape(user_regex) + '')
			# print(regex_to_use)
			expressions_found = []

			# stores each found exspresion
			for found in regex_to_use.findall(line):
				expressions_found.append(found)
			for i in range(len(expressions_found)):
				if expressions_found[i] != None:
				 	print('\tFile: ' + str(file) + '\n\tLine: ' + line + '\n\tExpression: ' + str(expressions_found))
				 	
				 	#store matches in a database
				 	shelf_expression_found[user_regex] = '\tFile: ' + str(file) + '\n\tLine: ' + line + '\n\tExpression: ' + str(expressions_found)
		shelf_expression_found.close()
					
	except UnicodeDecodeError:
		pass
	


# grab the arguemnts passed 
if len(sys.argv) == 2:
	open_cwd(sys.argv[1])
elif len(sys.argv) == 3:
	open_cwd(sys.argv[1], False)
else:
	# standard help message
	print('\nRegex_search.py <Regex> <Halt> - searches all files within the cwd (top-down) \nand below for the regex provided by the user.\nBy default the script searches all child directories, this can be limited to only the cwd by passing "Halt" as the second argument.')