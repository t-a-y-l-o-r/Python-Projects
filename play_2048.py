# play_2088.py - Will input up, right, down, left on the 2048 game until a game over occurs


import logging
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time

# debug your shit yo
def logger(file):
	logging.basicConfig(filename='file' ,level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

# searches for the passsed element until it is found
# can result in an infinite loop so use with caution
def find_element_by_class(browser, class_name):
	element = None
	while not element:
		try:
			time.sleep(3)
			element = browser.find_element_by_class_name(class_name)
		except Exception as exc:
			logging.warning(exc)
	return element

# runs mains operation
def main():
	browser = webdriver.Safari()
	browser.get('https://gabrielecirulli.github.io/2048/')
	

	# click the start button
	start_button = find_element_by_class(browser, 'restart-button')
	assert start_button, start_button
	start_button.click()

	#find the game board
	game_board = find_element_by_class(browser, 'game-container')
	assert game_board, game_board
	# up, right, down, left forever!
	while True:
		game_board.send_keys(Keys.UP)
		# time.sleep(2)
		game_board.send_keys(Keys.RIGHT)
		# time.sleep(2)
		game_board.send_keys(Keys.DOWN)
		# time.sleep(2)
		game_board.send_keys(Keys.LEFT)
		# time.sleep(2)
	time.sleep(10)
main()