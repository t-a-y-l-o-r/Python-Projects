# fill_the_gaps.py - Searches the cwd for all files with an intereger value. Determines if there is a gap in the intergers between different version, if a gap is found it is closed by renaming all of the files that were found after the cap



import os
import re
import shutil

name_regex = re.compile(r'''(
		\w+
		_+
		\d+
		([.]\w+)
		)''', re.VERBOSE | re.I)
integer_regex = re.compile(r'''(
	(\d)|(\d\d)|(\d\d\d)
	)''', re.VERBOSE)
one_integer_regex = re.compile(r'\d')
two_integer_regex = re.compile(r'\d\d')
three_integer_regex = re.compile(r'\d\d\d')
gaps = []
matches = []
foldername = ''
subfolders = ''
filenames = ''

def find_the_gap(folder):
	# Finds the gap in any file layout 
	print(folder)
	# grab all the file names that match our naming convention
	for foldername, subfolders, filenames in os.walk(folder):
		
		print('Searching Folder: ' + foldername)
		print('For gaps...')
		# grab all of the matches from the list
		for groups in name_regex.findall(str(filenames)):
			matches.append(groups[0])

		# check for any gaps among the matches
		for file in filenames:
			if three_integer_regex.search(file) is not None:
				findmatch(filenames, foldername, three_integer_regex)
			elif two_integer_regex.search(file) is not None:
				findmatch(filenames, foldername, two_integer_regex)
			else:
				findmatch(filenames, foldername, one_integer_regex)
	# print(matches)
	# print(gaps)

	
def findmatch(filenames, foldername, number_regex):
	number = 0
	for match in number_regex.finditer(str(filenames)):
		file = filenames[number]
		print('Match: ' + str(match.group()))
		print('Number: ' + str(number+1))
		print('Regex: ' + str(number_regex))
		if number == 1:
			break;
		if int(match.group()) is not (number+1):
			gaps.append(file)

			# rename all the files found after the gap
			for position in integer_regex.finditer(file):
				# print(position.start())
				# print('Old name: ' +  foldername + '/' + file)
				# print('New name: ' + foldername + '/' + file[ : position.start()] + str(number+1) + file[position.start()+1 : ] + '\n')
				if str(number_regex) == "re.compile('\\\\d')":
					# shutil.move(foldername + '/' + file, foldername + '/' + file[ : position.start()] + str(number+1) + file[position.start()+1 : ])
					print('File name contains single digit.')
					print('Match: ' + match.group() + '\n')
				elif str(number_regex) == "re.compile('\\\\d\\\\d')":
					# shutil.move(foldername + '/' + file, foldername + '/' + file[ : position.start()] + str(number+1) + file[position.start()+1 : ])
					print('File name contains double digits' + '\n')
					print('Match: ' + match.group() + '\n')
				elif str(number_regex) == "re.compile('\\\\d\\\\d\\\\d')":
					# shutil.move(foldername + '/' + file, foldername + '/' + file[ : position.start()] + str(number+1) + file[position.start()+1 : ])
					print('File name contains tripple digits' + '\n')
				# CURRENT PROBLEM: THIS SHIT IS FUCKED YO
				'''
				Known issues:
					1) Can't handle multiple digit integers in file names properly;
						- as in it only alters the first integer instead of the entire integer
					2) It deleted some of the folders by moving one folder onto one that already exits
					3) 
				'''
		if number < len(filenames)-1:
			number += 1



find_the_gap('/users/taylorcochran/desktop/_folder/computer/programming/python/automate the boring/blarg_zips')