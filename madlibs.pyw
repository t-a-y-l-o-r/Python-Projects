# madlibs.pyw - Allows the user to replace nouns, adjs, verbs, and adverbs from an 
# madlib file
# python3 madlibs.pyw <madlib_file.txt> - Will prompt the user to replace all occurences of 
# 										   NOUN, ADJECTIVE, ADVERB, and VERB in the 
#										   madlib_file.txt


import re
import sys
import os

noun_regex = re.compile(r'NOUN')
adj_regex = re.compile(r'ADJECTIVE')
verb_regex = re.compile(r'VERB')
adverb_regex = re.compile(r'ADVERB')


# target file is passed as the sys arg
if len(sys.argv) == 2:
	lib_file = open(os.path.join(os.getcwd(), sys.argv[1]))
	new_file = open(os.path.join(os.getcwd(), 'madlibs_folder/new_file.txt'), 'w')

	# grabs each line from the file
	for line in lib_file.readlines():
		print('\n' + line)
		# search each line for any matches
		# replace the matches
		if noun_regex.search(line) != None:
			print('Enter a noun: ')
			user_noun = input()
			line = noun_regex.sub(user_noun, line)
		if verb_regex.search(line) != None:
			print('Enter a verb: ')
			user_verb = input()
			line = verb_regex.sub(user_verb, line)
		if adj_regex.search(line) != None:
			print('Enter an adjective: ')
			user_adj = input()
			line = adj_regex.sub(user_adj, line)
		if adverb_regex.search(line) != None:
			print('Enter an adverb: ')
			user_adverb = input()
			line = adverb_regex.sub(user_adverb, line)
		new_file.write(line)		
		# print the new string
		# save new string to a new file
	lib_file.close()
	new_file.close()
	new_file = open(os.path.join(os.getcwd(), 'madlibs_folder/new_file.txt'))
	print('\n' + new_file.read())

# help message
else:
	print('madlibs.pyw <target_file> - Will allow the user to substitue\nouns, adjs, and so on in the target_file.')