# box_print.py - Let's learn about exceptions!


def box_print(symbol, width, height):
	if len(symbol) is not 1:
		raise Exception('Symbol must be a single char string!')
	if width <= 2:
		raise Exception('Width must be greater than two!')
	if height <= 2:
		raise Exception('Height must be greater than two!')

	# prints the symbol entered by the user, with the given params
	print(symbol * width)
	for i in range(height -2):
		print(symbol + (' ' * (width - 2)) + symbol)
	print(symbol * width)


# Apparenlty you can execute multiple instances of a function with for
for sym, w, h in (('*', 4, 4), ('0', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
	try:
		box_print(sym, w, h)
	except Exception as err:
		print('An exception occured: ' + str(err))
