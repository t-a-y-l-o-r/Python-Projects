# backup_to_zip.py - Backsup snapshots of files  as zipfolders, incrementing the filename version with each snapshop



import zipfile
import os


def backup_to_zip(folder):
	# Backup the contents of a folder

	# Folder var now includes the entire path name :>
	folder = os.path.abspath(folder)

	# Determine which version of the zipfolders already exist
	number = 1
	while 1:
		zip_filename = os.path.basename(folder) + '_' + str(number) + '.zip'
		if not os.path.exists(zip_filename):
			break
		number += 1

	# Create the zip file
	print('Creating %s...' % (zip_filename))
	backup_zip = zipfile.ZipFile(zip_filename, 'w')

	# Walk the entire folder tree (top-down) and compress the files in each folder:
	for foldername, subfolders, filenames in os.walk(folder):
		print('Adding files in %s...' % (foldername))
		# Add the current folder to the zip file 
		backup_zip.write(foldername)
		# Add all the files in this folder to the Zip folder
		for filename in filenames:
			# grab the folder name and add an underscore to it
			# basename takes the second arguement returned by split()
			# split returns the abs dir and the folder name 
			# basename takes the folder name
			new_base = os.path.basename(folder) + '_'
			if filename.startswith(new_base) and filename.endswith('.zip'):
				continue # won't backup the already backuped files 
			backup_zip.write(os.path.join(foldername, filename))
	print('Abs: ' + os.path.abspath(str(backup_zip)))
	backup_zip.close()
	print('Done!')
		




folder = '/users/taylorcochran/desktop/blarg'
backup_to_zip(folder)