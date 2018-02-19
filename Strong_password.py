# Strong_password.py - tests the strength of a password
'''
minimun 8 chars
at least 1 number
at least one upper case
at least one lower case

'''


import re

# must be 8 chars long
password_check_length = re.compile(r'''(
	([a-zA-Z0-9]{8,}) 
	)''', re.VERBOSE)

# checks the passed string for any integers
password_check_digits =re.compile(r'[0-9]')

#checkes the passed string for any upper case letters
password_check_upper = re.compile(r'[A-Z]')

#checks the passed string for any lower case letters
password_check_lower = re.compile(r'[a-z]')


password = 'Thisasdad1ASDawdw311212'
strong = False


passwords = ['dasiudbaskdb', 'asoduabd2113231ASDAS', 'santaIsCOmingTOTown', 'hoWdy1111asa']


# test the strength of a password argument 
def test_pass_strength(password):
	digit = False
	upper = False
	lower = False
	
	# at least 8 char
	if (password_check_length.search(password) != None):
		for i in range(len(password)):

			# if the password has digits, upper, and lower then it's good
			if ((digit and upper) and lower):
				print(password + " is a strong password.")
				break

			# if not and we're at the last char then the pass fails
			elif (not((digit and upper) and lower)) and (password[i] == password[-1]):
				print(password + 'is a weak password.')
				break

			# at least one digit
			if password_check_digits.search(password[i]) != None:
				digit = True
				continue

			# some upper case
			if password_check_upper.search(password[i]) != None:
				upper = True
				continue

			# some lower case
			if password_check_lower.search(password[i]) != None:
				lower = True
				continue
	else:
		print(password + " is a weak password.")

#test_pass_strength(password)

for i in range(len(passwords)):
	test_pass_strength(passwords[i])