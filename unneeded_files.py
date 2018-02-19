# unneeded_files.py - Searches the cwd for any file greater than 100MB and prints the folder, filename, and size to standard out

import os

def search_my_shit(cwd):
	os.chdir(cwd)
	for folder, subfolders, files in os.walk(cwd):
		for file in files:
			if os.path.isfile(folder + '/' + file):
				size = os.path.getsize(folder + '/' + file)
				if (size >= 100000000):
					print('Folder: ' + folder)
					if len(file) > 15:
						print('\t File: ' + file[:15] + '\t\tSize: ' + str(size))
					elif len(file) < 10:
						print('\t File: ' + file + '\t\t\tSize: ' + str(size))
					else:
						print('\t File: ' + file + '\t\tSize: ' + str(size))
search_my_shit('/users')