# search_shit.py - Opens the first several google results in seperate tabs
'''
A simple and straight forward script for opening the first five links (or fewer)
from a google search in your browser
Not much to change here, except perhaps displaying the search page 
'''

import requests, sys, webbrowser, bs4

print('Googling...')
request = requests.get('https://google.com/search?q=' + ' '.join(sys.argv[1:]))
request.raise_for_status() # will raise error if the request failed

google_soup = bs4.BeautifulSoup(request.text, 'html.parser')
link_elements = google_soup.select('.r a')

# for i in range(len(link_elements)):
# 	if i >= len(link_elements)-1:
# 		break
# 	else:
# 		print('\tOpening link: ' + link_elements[i+1].getText())

number_to_open = min(5, len(link_elements))
for i in range(number_to_open):
	if i == number_to_open:
		break
	else:
		webbrowser.open('https://google.com' + link_elements[i+1].get('href'))