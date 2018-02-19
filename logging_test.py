# Here we learn about the logging module and how to implement it in a basic factorial funciton

# Allows for logging sheet
import logging
# disables all logging following this line of code 
# of a level equal to or lower than the var passed 
# (DEBUG < INFO < WARNING < ERROR <  CRITICAL)
# logging.disable(logging.CRITICAL)

# logging level canresitric which messages are shown by calling logging, allowing for 
# greater control over logging needs
# ie debug now, info and crash handling latter 
logging.basicConfig(filename='logging_test_log_file.txt' ,level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program.')

def factorial(n):
	logging.debug('Start of factorial (%s%%)' % (n))
	total = 1
	for i in range(1, n + 1):
		total *= i
		logging.debug('i is ' + str(i) + ', total is ' + str(total))
	logging.debug('End of factorial (%s%%)' % (n))
	return total

print(factorial(5))
logging.debug('End of program.')