#! /usr/bin/env python3
# This program will be a basic demonstration of a password vault
# this program is not secure 

import sys
import pyperclip

PASSWORDS = {
		'email': '464asd54asd3a4d',
		'blog': 'ada43dw35da5d1',
		'luggage': 'asd41a35d1w' }


if len(sys.argv) < 2:
	print('Usage: python pw.py [account] - copy account password')
	sys.exit()

account = sys.argv[1] 	# account name 


if account in PASSWORDS:
	pyperclip.copy(PASSWORDS[account])
	print('Password for ' + account + ' copied to clipboard.')
else:
	print('There is no account named ' + account)