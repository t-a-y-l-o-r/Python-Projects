#! usr/bin/env python3

'''
Goal: To add starts bullets to a list of lists 

1) Paste text from clipboard 
2) Add stars
3) Copy modified text to the clipboard 
'''


import pyperclip
text = pyperclip.paste()

# sperate lines and adds stars
lines = text.split('\n')
for i in range(len(lines)): # loop through each line in the new list of lines
	lines[i] = '* ' + lines[i] # add a star to the beging of each line

text = '\n'.join(lines)

pyperclip.copy(text)