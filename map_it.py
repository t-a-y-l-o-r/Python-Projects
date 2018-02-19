# map_it.py <address> will bring up the passed address on google maps
# if no argument is passed the address is pulled from the clipboard

import sys
import webbrowser
import pyperclip
import re
import logging

logging.basicConfig(filename='map_it_logfile.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

web_address_regex = re.compile(r'''(
	(http(s)?)
	(:)
	(//)
	(www)([.])
	(\w+)
	([.]com)
	(/[A-Za-z0-9/]*)?
	)''', re.VERBOSE)
# https://www.google.com/helloworlf/dy/819y31
'''
	group zero is the entire string
	(http(s)?) (1(2))
	(:)			(3)
	(//)		(4)
	(www)([.])	(5)(6)
	(\w+)		(7)
	([.]com)	(8)
	(/[A-Za-z0-9/]*)?	(9)
'''

street_address_regex = re.compile(r'''(
	(\d)+
	(\s)
	(\w)+
	(\s)
	(\w)+
	(\s)
	(\w)*
	(\s)*
	(\w)+
	([,])
	(\s)
	(\w){2}	
	(\s)
	(\d){5}
	)''', re.VERBOSE | re.I)
'''
	761 Venus View Drive Vista, Ca 92081
	(\w)+
	(\s)?

	(\w)*
	(\s)?

	(\w)*
	(\s)?

	(\w)*
	[,]

	(\w){2}
	(\s)?

	([0-9]{5})

'''


address = ''
if len(sys.argv) > 1:
	# Grabs the address from the command line arg
	if web_address_regex.findall(' '.join(sys.argv[1:])):
		address = ' '.join(sys.argv[1:])
	elif street_address_regex.findall(' '.join(sys.argv[1:])):
		address = ' '.join(sys.argv[1:])
else:
	# Grabs the address from the clipboard
	if web_address_regex.findall(pyperclip.paste()):
		address = pyperclip.paste()
	elif street_address_regex.findall(pyperclip.paste()):
		address = pyperclip.paste()


# ensure the script has a proper address before continuing
assert address, 'No proper address found! Please try again.'
logging.debug('Address: ' + address)


# opens your shit
if web_address_regex.findall(address):
	webbrowser.open(address)

elif street_address_regex.findall(address):
	webbrowser.open('https://www.google.com/maps/place/' + address)





