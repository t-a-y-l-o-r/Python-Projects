# blank_row_inserter.py <N> <M> <filename.xlsx> - inserts M rows below row N inside the filename.xlsx spreadsheet 

'''
This feels like my first "simple and elegent" script, granted the task at hand was simple in of itself.
'''

import openpyxl
import sys

if len(sys.argv) == 4:
	starting_row = int(sys.argv[1])
	blank_rows = int(sys.argv[2])
	work_book = openpyxl.load_workbook(str(sys.argv[3]))
else:
	print('\nblank_row_inserter.py <N> <M> <filename.xlsx> - inserts M rows below row N inside the filename.xlsx spreadsheet ')


sheet = work_book.active
for i in range(1, sheet.max_row+1): # range discludes the top int 
	# for every row beyond the starting row shift down by the number of rows passed 
	if i > starting_row:
		for cell in sheet[i]:
			cell.row += blank_rows
# always save in a new file
work_book.save('blanks.xlsx')