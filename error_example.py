
import traceback


def spam():
	bacon()

def bacon():
	try:
		raise Exception('This is an error message.')
	except:
		error_file = open('error_file.txt', 'w')
		error_file.write(traceback.format_exc())
		error_file.close()
		print('The traceback info was written to error_file.txt')

spam()