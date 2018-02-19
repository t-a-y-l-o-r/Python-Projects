# emailer_2.py - the autamted email service that actually works! (let's hope)
# emailer_2.py <email> promps the user for a subject and body message, then send the email to the passed argument
'''
Some reddit user
2017/7/15
Problem:
	Emails are boring 
Algorythm:
	1) Pull email from sys.argv[1]
	2) Prompt user for subject and main message - store for later 
	3) Using webdriver navigate your chosen browser to your prefered email provider 
	4) Long in using element.send_keys(name) and elem.send_keys(pass)
		- gotta inspect the website elements for this to work
		- use webdriver.find_element_by_class_name(class_name)
		- get angry when the class you copied is missing a single underscore
	5) Open a new email using element.send_keys('\n') or element.click()
	6) Fill in email using emailer name provided by sys.argv[1] using elem.send_keys(email)
	7) Find element class of subject, subject_elem.send_keys(subject)
	8) Repeat step 7 for main body message
	9) Find element of send button, send_elem.click()
		- rage when there are two send buttons but only one works
		- doubt your email was sent
		- delete all 200 failed drafts created during debugging process
		- have fun!
'''
'''
	To DO:
		1) Send the message - done
		2) Pull email from argv[1] - done
		3) Prompt user for subject and message - done
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import logging
import time
import sys

def logger(file):
	logging.basicConfig(filename=file, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def open_browser():
	browser = webdriver.Safari()
	return browser

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
	logging.debug('Tried to find: ' + find_this_class + '\n' + str(i) + 'times.')
	return element


def main():
	# shit might change latter, best to keep it modular for now
	file = 'emailer_logger.txt'
	website = 'https://hotmail.com'
	username = 'this_is_my_email@email.fake.com'
	password = 'bro_enter_your_own_shit'
	# to_this_email = 'not_real@gmail.com'
	if len(sys.argv) == 2:
		to_this_email = sys.argv[1]
	# subject_field_message = 'Testing 1 2 3'
	subject_field_message = input('Subject: ')
	# main_message = 'Hello World!!'
	main_message = input('Main message: ')
	'''
	The following classes will change depending on the webpage!
	This is not a general use script future me!
	'''
	username_class = 'placeholder'
	password_class = 'placeholder'
	create_new_email_class = '_fce_h _fce_f ms-fwt-r ms-fcl-np o365button'
	to_this_email_class = '_fp_G ms-fwt-r ms-font-color-neutralSecondary allowTextSelection ms-bgc-nl textbox ms-font-s ms-fwt-sl ms-fcl-np ms-bcl-nta ms-bcl-nsa-h hideClearButton ms-fcl-ns'
	subject_field_class = '_mcp_Q1 _mcp_R1 ms-font-weight-regular ms-bg-color-white-hover ms-font-color-neutralPrimary allowTextSelection _mcp_S1 textbox ms-font-s ms-fwt-sl ms-fcl-np ms-bcl-nta ms-bcl-nsa-h'
	main_message_field_class = 'allowTextSelection ConsumerCED _mcp_32 customScrollBar ms-bg-color-white ms-font-color-black owa-font-compose'
	send_class = 'label o365buttonLabel _fce_r _fce_n'


	# debugging is fun
	logger(file)
	# basic shit
	browser = open_browser()
	browser.get(website)
	actions = ActionChains(browser)



	# we really need the browser to work yo
	assert browser is not None
	logging.debug('Website: ' + website + '\nDriver: ' + str(browser))

	#enter the username
	username_element = find_element_by_class(browser, username_class, username)
	assert username_element, username_element
	logging.debug('Username element: ' + str(username_element) + '\nUserName: ' + str(username))
	# username_element.send_keys(username + '\n')

	#enter the password
	password_element = find_element_by_class(browser, password_class, password)
	assert password_element, password_element
	logging.debug('Password element: ' + str(password_element) + '\nPassword: ' + str(password))
	# password_element.send_keys(password + '\n')

	#open a new email
	create_new_email_element = find_element_by_class(browser, create_new_email_class)
	assert create_new_email_element, create_new_email_element
	create_new_email_element.click()
	logging.debug('New Email element: ' + str(create_new_email_element) + '\nNew has been clicked')

	#Enter the email address
	to_this_email_element = find_element_by_class(browser, to_this_email_class, to_this_email)
	# why is this field being annoying??
	actions.send_keys(to_this_email)
	actions.perform()
	assert to_this_email_element, to_this_email_element
	logging.debug('To this email element: ' + str(to_this_email_element) + '\nTo this email: ' + to_this_email)

	#Enter the subject!
	subject_field_element = find_element_by_class(browser, subject_field_class, subject_field_message)
	assert subject_field_element, subject_field_element
	logging.debug('Subject element: ' + str(subject_field_element) + '\nSubject: ' + subject_field_message)

	#Enter the main message
	main_message_field_element = find_element_by_class(browser, main_message_field_class, main_message)
	assert main_message_field_element, main_message_field_element
	logging.debug('Main message element: ' + str(main_message_field_element) + '\nMain message: ' + main_message)

	#Send the message!
	send_message_element = find_element_by_class(browser, send_class)
	assert send_message_element, send_message_element
	send_message_element.click()
	logging.debug('Send message element: ' + str(send_message_element) + '\nSend message clicked.')
	# for debugging purposes
	# time.sleep(10)
main()