#! usr/bin/env python3 
'''
This program defines a function that accepts a list of lists 
Each inner list is of strings 
The function should print a formatted table with each column right justified 
'''

list_of_lists = [
	['apples', 'oranges', 'cherries', 'banana'],
	['Alice', 'Bob', 'Carol', 'David'],
	['dogs', 'cats', 'moose', 'goose'] ]

def print_table(list_of_lists):
	#finds the largest string from the list of lists 
	largest_string_str = ''
	for i in range(len(list_of_lists)):
		if i == 0:
			largest_string_str = largest_string(list_of_lists[i])
		else:
			if len(largest_string_str) < len(largest_string(list_of_lists[i-1])):
				largest_string_str = largest_string(list_of_lists[i-1])
	# justification for largest string 			
	just = len(largest_string_str)
	#prints out the grid right justified based on largest string 
	for i in range(len(list_of_lists)):
		for q in range(len(list_of_lists[i])):
			print(list_of_lists[i][q].rjust(just) + ' ', end='')
		print() # adds a new line after each list ends





# finds the largest string in a list of strings
def largest_string(list):
	for i in range(len(list)):
		if i == 0:
			largest_string_str = list[i] 
		else:
			if len(largest_string_str) < len(list[i]):
				largest_string_str = list[i]
	return largest_string_str

print_table(list_of_lists)