# Phone_address.py - Finds phone numbers and email address on the clipboard

import re
import pyperclip

phone_regex = re.compile(r'''(
	(\d{3}|\(\d{3}\))?				# area code 
	(\s|-|\.)						# seperator
	(\d{3})							# first three digits
	(\s|-|\.)						# seperator
	(\d{4})							# last four digits
	(\s*(ext|x|ext.)\s*(\d{2,5}))?	# extension
	)''', re.VERBOSE)

email_regex = re.compile(r'''(
	[a-zA-Z0-9._%+-]+ 		#username
	@ 						# @ symbol
	[a-zA-Z0-9._%+-]+ 		# domain name
	(\.[a-zA-Z]{2,4}) 		# top-level domain
	)''', re.VERBOSE)


# emails and numbers stored in the clipboard
text = str(pyperclip.paste())

matches = []
for groups in phone_regex.findall(text):
	phone_number = '-'.join([groups[1], groups[3], groups[5]])
	# phone_number = groups[0] would take in many formates 
	# the number is equal to the first numbers - second numbers - third numbers 
	# joining the individual groups allows for a standardized format
	if groups[8] != '':
		phone_number += 'x' + groups[8]
		# extension
	matches.append(phone_number)

for groups in email_regex.findall(text):
	matches.append((groups[0]))
	# all matches 


# now to output everything to the clipboard
if len(matches) > 0:
	pyperclip.copy('\n'.join(matches))
	print('Copied data to clipboard.')
	print('\n'.join(matches))
else:
	print('No numbers or addresses found.')