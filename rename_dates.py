# rename_dates.py - Searches the cwd for files with Amercian dates, changes the names to a European format and moves the files. 
# MM-DD-YYYY -> to DD-MM-YYYY



import os
import shutil
import re


#Create a regeex that matches the files with the American date format
date_pattern = re.compile(r'''
	^([^0-9]*?)		# all text before the date
	((0|1)?\d)-		# one or two digits for the month
	((0|1|2|3)?\d)- # one or two digits for the day
	((19|20)?\d\d)  # four digits for the year/ or two for the year
	(.*?)$			# the file extension
	''', re.VERBOSE)
'''
date_pattern = re.compile(r"""
	^(1)		
	(2 (3))-		
	(4 (5))-
	(6 (7))
	(8)$	
	""", re.VERBOSE)
'''

def search_cwd_dates():
	for amer_filename in os.listdir():
		# work with the files that do match
		mo = date_pattern.search(amer_filename)

		# skip the files that don't match
		# prevents any exceptions that would occur down the line
		if mo is None:
			continue
		# else:
		# 	for i in range(len(mo.groups())):
		# 		print('i: ' + str(i) + ' ' + mo.group(i))

		'''
		When stores groups found by re.compile(r'').search() function
		make sure to skip the groups that return only the optionally included 
		content. Usually you want the entire section found, not just part of it.
		For proof simply run the above else statment
		'''
		before_part = mo.group(1)
		month_part = mo.group(2)
		# group(3) would return the optional match only
		day_part = mo.group(4)
		# group(5) would do the same 
		year_part = mo.group(6)
		# group(7) is the same way
		after_part = mo.group(8)


		#Form the European-style filename
		euro_filename = before_part + day_part + '-' + month_part + '-' + year_part + after_part


		#Get the full, absolite file paths

		abs_dir = os.path.abspath('.')
		amer_filename_abs = os.path.join(abs_dir, amer_filename)
		euro_filename_abs = os.path.join(abs_dir, euro_filename)

		# Rename the file
		print('Renameing %s to "%s"...' % (amer_filename, euro_filename))
		shutil.move(amer_filename_abs, euro_filename_abs)





search_cwd_dates()


























