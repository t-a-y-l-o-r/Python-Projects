# selective_copy.py - Copies files with a .txt extension from their current location to a location of the user's choosing


import os
import shutil


def selective_copy(folder):
	# give the exact location of the passed folder
	folder = os.path.abspath(folder)

	# walk the cwd (top-down)
	print('Files found and copied: ')
	for foldername, subfolders, filenames in os.walk(folder):
		# we're only interested in the files
		for filename in filenames:
			# more so the text files
			if filename.endswith('.txt'):
				print('\t-) ' + filename)
				filename = foldername + '/' + filename
				shutil.copy(filename, '/users/taylorcochran/text_files')

selective_copy('/users/taylorcochran/desktop/blarg')