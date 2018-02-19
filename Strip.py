# Strip.py - removes things from the passed argument
'''
python3 Strip.py arv1 arv2
av1 - string to strip
arv2 - char to strip from string // if blank whitespace is stripped
'''


import re
import sys

space_regex = re.compile(r'\s') # white space
num_regex = re.compile(r'\d+') # numbers
char_regex = re.compile(r'[a-z]+', re.I) # letters/ ignores case
symbol_regex = re.compile(r'[!@#$%\^&*()\\|\[\]{};:\'"~`]+')

def remove_whitespace(stringy):
	'''
	The purpose here is to recreate the string with each iteration
	as a smaller string without the current found white space.
	This is done by splicing the 'orginal' string and 
	reassigning it. This will continue for the entire length 
	of the string, and will adust dynamically with the changing 
	length of the string after each slice.
	The original design contained a for loop which failed to account 
	for the length of the string changing and thus would always 
	return an index error. Simply changing to a while loop fixed this bug.
	'''
	i = 0
	# removes any white space at the begining of the string
	while (space_regex.search(stringy[i]) != None):
		stringy = stringy[i+1:]
	# removes any white space at any other point in the string
	while (i <= len(stringy)-1):
		i += 1
		# when there's a match
		while (space_regex.search(stringy[i-1]) != None):
			# remove the match
			stringy = stringy[0:i-1] + stringy[i:]
			# skip the the next loop
			continue
	# whitespace not included!
	return stringy


# CURRENT ISSUE: REMOVING MULTIPLE DIGIT VALUES FROM THE STRING
def remove_something_else(stringy, something_else):
	if not isinstance(something_else, str):
		something_else = str(something_else)
	if not isinstance(stringy, str):
		stringy = str(stringy)
	i = 0
	print('String to strip: ' + stringy)
	print('Striping: ' + something_else)

	# if the argv2 passed is an int
	if num_regex.search(something_else) != None:
		# easier to remove a single value
		if len(something_else) == 1:
			while ( something_else == stringy[i] ):
				stringy = stringy[i+1:]
			# prevents index error
			while ( i < len(stringy)-len(something_else) ):
				i += 1
				# while the passed int is the same as the slice, remove the slice
				while (stringy[i] == something_else):
					stringy = stringy[0:i] + stringy[i+1:]
		else:
			# removes all matching ints from the begining of the passed string
			while ( something_else == stringy[i:i+(len(something_else))] ):
				stringy = stringy[i+(len(something_else)):]
			# prevents index error
			while ( i < len(stringy)-len(something_else) ):
				i += 1
				# while the passed int is the same as the slice, remove the slice
				while (stringy[i:i+len(something_else)] == something_else):
					stringy = stringy[0:i] + stringy[i+len(something_else):]

	elif char_regex.search(something_else) != None:
		# easier to remove a single value
		if len(something_else) == 1:
			while ( something_else.upper() == stringy[i].upper() ):
				stringy = stringy[i+1:]
			# prevents index error
			while ( i < len(stringy)-len(something_else) ):
				i += 1
				# while the passed int is the same as the slice, remove the slice
				while ( stringy[i].upper() == something_else.upper() ):
					stringy = stringy[0:i] + stringy[i+1:]
		else:
			# removes all matching chars from the begining of the passed string
			while ( something_else.upper() == stringy[i:i+(len(something_else))].upper() ):
				stringy = stringy[i+(len(something_else)):]
			# prevents index error
			while ( i < len(stringy)-len(something_else) ):
				i += 1
				# while the passed char is the same as the slice, remove the slice
				while ( stringy[i:i+len(something_else)].upper() == something_else.upper() ):
					stringy = stringy[0:i] + stringy[i+len(something_else):]

	elif symbol_regex.search(something_else) != None:
		# easier to remove a single value
		
		if len(something_else) == 1:
			while ( something_else == stringy[i] ):
				stringy = stringy[i+1:]
			# prevents index error
			while ( i < len(stringy)-len(something_else) ):
				i += 1
				# while the passed int is the same as the slice, remove the slice
				while (stringy[i] == something_else):
					stringy = stringy[0:i] + stringy[i+1:]
		else:
			# removes all matching ints from the begining of the passed string
			while ( something_else == stringy[i:i+(len(something_else))] ):
				stringy = stringy[i+(len(something_else)):]
			# prevents index error
			while ( i < len(stringy)-len(something_else) ):
				i += 1
				# while the passed int is the same as the slice, remove the slice
				while (stringy[i:i+len(something_else)] == something_else):
					stringy = stringy[0:i] + stringy[i+((len(something_else))-1):]

	return stringy





hello = '     Hello World       goodbye'
number_string = '55454565555555555556555235432523523'
symbol = '@@@@@!@#$#%$%$^$!%$#@$#@$'

# print(remove_whitespace(hello))
# print(remove_something_else(number_string, 5))
# print(remove_something_else(hello, 'oo'))
# print(remove_something_else(symbol, '@'))

if len(sys.argv) == 2:
	print(remove_whitespace(argv[1]))
elif len(sys.argv) == 3:
	print(remove_something_else(sys.argv[1], sys.argv[2]))
else:
	print('Usage: py Strip.py [string] [remove] \n\tString- string to strip \n\tRemove - char/num/symbol to remove. \n\tIf blank then white space is removed')










