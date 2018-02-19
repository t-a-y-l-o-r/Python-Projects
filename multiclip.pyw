# multiclip.pyw - Saves and loads pieces of text to the clipboard
# Usage: py.exe multiclip.pyw save <keyword> - Saves keyword to the clipboard
# 		 py.exe multiclip.pyw <keyword> - Loads keyword to clipboard
#		 py.exe multiclip.pyw list - Loads all keywords to clipboard
#  		 py.exe multiclip.pyw del <keyword> - Deletes the keyword from the shelf

import shelve
import pyperclip
import sys

multiclip_shelf = shelve.open('multiclip')

#Save clipboard content 
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
	multiclip_shelf[sys.argv[2]] = pyperclip.paste()
# delets the keyword from the shelf
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'del':
	del multiclip_shelf[sys.argv[2]]
elif len(sys.argv) == 2:
	#List keywords and save content:
	if sys.argv[1].lower == 'list':
		pyperclip.copy(str(list(multiclip_shelf.keys())))
	elif sys.argv[1] in multiclip_shelf:
		pyperclip.copy(multiclip_shelf[sys.argv[1]])





multiclip_shelf.close()