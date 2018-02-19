# properly_fill_gaps.py - Fills gaps in your files number scheme. Gaps are filled by renaming all following files until all gaps are filled.




import re
import os
import shutil
import pprint


def my_regexs(regex_request=None):
	# Defines the regexs used in this program 
	digit_re = re.compile(r'\d+')
	filename_re = re.compile(r'''(
		^(\w+)_\d+([.]\w+)$
		)''', re.VERBOSE)
	if regex_request == 1:
		return digit_re
	else:
		return filename_re


def walk_cwd(cwd):
	# Walks the cwd and stores all filename matches along with their paths in a dict
	cwd = os.path.abspath(cwd)
	naming_matches = {}
	filename_re = my_regexs()
	for foldername, subfolders, filenames in os.walk(cwd):
		for file in filenames:
			if filename_re.search(file):
				naming_matches[str(file)] = str(foldername)
	find_gaps(naming_matches)


def find_gaps(naming_matches):
	# Finds all gaps in the matched names 
	# Starts by breaking up the names into three groups 
	# Find gaps from the lowest number up, filling gaps as it goes
	digit_re = my_regexs(1)
	name_matches = {}
	digit_matches = {}
	for filename in naming_matches.keys():
		if digit_re.search(filename):
			name_matches[filename] = naming_matches[filename]

	# dict of the individual integers found by the regex
	for key in name_matches.keys():
		digit = int(digit_re.findall(key)[0])
		digit_matches[digit] = key
	# plug all the gaps
	fill_gaps(name_matches, digit_matches)
	

def fill_gaps(name_matches, digit_matches):
	# Fills the gaps in the naming convention
	digit_re = my_regexs(1)
	number = 1
	# Grabs the old file name from matches list
	for digit in sorted(digit_matches.keys()):
		# Finds the position of the digit
		if digit != number:
			filename_new = digit_re.sub(str(number), digit_matches[digit])
			number += 1
			# Errors are gross
			if os.path.exists(name_matches[digit_matches[digit]] + '/' + digit_matches[digit]):
				shutil.move(name_matches[digit_matches[digit]] + '/' + digit_matches[digit], name_matches[digit_matches[digit]] + '/' + filename_new)
		else:
			number += 1

walk_cwd(os.getcwd())