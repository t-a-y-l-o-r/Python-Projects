

# determins if the passed string is a phone number or not 
def is_phone_number(text):
	if len(text) != 12:
		return False
	for i in range(0, 3):
		if not text[i].isdecimal():
			return False
	if text[3] != '-':
		return False
	for i in range(4, 7):
		if not text[i].isdecimal():
			return False
	if text[7] != '-':
		return False
	for i in range(8, 12):
		if not text[i].isdecimal():
			return False
	return True


# test statments
# print('415-555-4242 is a phone number:')
# print(is_phone_number('415-555-4242'))
# print('Moshi moshi is a phone number: ')
# print(is_phone_number('Moshi moshi'))

#better version of testing:
message = 'Call me at 415-555-4242 tomorrow. 415-555-4242 is my office'

for i in range(len(message)):
	chunk = message[i:i+12]
	if is_phone_number(chunk):
		print('Phone numbe found: ' + chunk)
print('Done')



# The regular expression form of the above is:
'''
import re
phone_num_regex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phone_num_regex.search('My number is 415-555-4242')
print('Phone number found: ' + mo.group())
'''