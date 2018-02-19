# imgur_downloader.py <search_this> - Searches the passed arg on imgur and downloads all of the resulting images
'''
Some redditor
2017/07/16

Problem:
	Pictures are on the internet and not on my hardrive
Algorythm:
	1) Naviagte to a webpage - like imgur or instagram
	2) Search something 
	3) Grab a list of all images results
	4) Pull the src of each individual img and download to a dir tree:
		- website/thing_you_searched
	5) ???
	6) Profit
'''


import sys
import time 
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import logging
import requests
import os

# debugging shit
def logger(file):
	logging.basicConfig(filename=file, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# cuz
def open_browser():
	browser = webdriver.Safari()
	return browser

# allows for navigation of the things
def find_element_by_class(browser, find_this_class, keys_to_send=None):
	element = None
	i = 0
	while not element:
		try:
			time.sleep(4)
			element = browser.find_element_by_class_name(find_this_class)
			i += 1
			# enter the passed string to the current selected element field
			if keys_to_send:
				element.send_keys(keys_to_send + '\n')
				logging.debug('Entering these keys: ' + keys_to_send)
		except Exception as exc:
			logging.warning(exc)
	logging.debug('Tried to find: ' + find_this_class + '\n' + str(i) + ' times.')
	return element

# allows for navigation of multiple things with the same class name
def find_elements_by_class(browser, find_this_class):
	elements = None
	i = 0
	while not elements:
		try:
			time.sleep(4)
			elements = browser.find_elements_by_class_name(find_this_class)
			i += 1
		except Exception as exc:
			logging.warning(exc)
	logging.debug('Tried to find:' + find_this_class + '\n' + str(i) + ' times')
	return elements


def main():
	logger('imgur_log.txt')
	browser = open_browser()
	# imgur website
	browser.get('https://imgur.com')
	

	#basic vars
	search_this = 'hello world'
	if len(sys.argv) == 2:
		search_this = sys.argv[1]

	#dirs
	os.makedirs('imgur/' + search_this, exist_ok=True)

	# classes 
	icon_class = 'icon-search'
	image_class = 'image-list-link'


	# finds the search bar and searches the 'search_this' thingy
	icon_element = find_element_by_class(browser, icon_class)
	assert icon_element, icon_element
	logging.debug('Icon Element: ' + str(icon_element) + '\nClicking search!')
	icon_element.click()
	icon_element.send_keys(search_this + '\n')


	# list of all images found 
	image_elements = find_elements_by_class(browser, image_class)

	# grab the each image from the list of image
	for image_element in image_elements:
		# source link
		source = image_element.find_element_by_css_selector('img').get_attribute('src')
		logging.debug('Image Source: ' + str(source))
		# grab the data from the source link
		image_request = requests.get(source)
		# check for errors
		image_request.raise_for_status()

		# write the image file to disk
		image_file = open(os.path.join('imgur/' + search_this, os.path.basename(source)), 'wb')
		for chunk in image_request.iter_content(100000):
			image_file.write(chunk)
		image_file.close()
		break
main()