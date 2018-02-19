# verify_links.py <url> will verify every link on a the passed url, any broken links will be printed to screen :>

import time
import requests 
import sys
import bs4


def main(url):
	# grab page
	webpage_request = requests.get(url)
	webpage_request.raise_for_status()
	webpage_soup = bs4.BeautifulSoup(webpage_request.text, 'html.parser')

	# find everything
	# find all the things inside of the body
	try:
		for thingy in webpage_soup.findAll('a'):
			if thingy.has_attr('href'):
				# grab all links
				page_request = requests.get( str( url + thingy.get('href') ) )
				# only print the broken ones
				if page_request.raise_for_status() is not None:
					print('Broken link: \n' + str(url + thingy.get('href')) )
					print(str(page_request.raise_for_status()) + '\n')
	except Exception as exc:
		pass
	print('All links tested!')
		



url = 'https://nostarch.com'
if len(sys.argv) == 2:
	url = sys.argv[1] 
main(url)