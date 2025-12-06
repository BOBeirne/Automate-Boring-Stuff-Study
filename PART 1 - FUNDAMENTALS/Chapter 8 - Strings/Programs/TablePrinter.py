# Write a function printtable() that takes list of lists of strings and displays them in well organized table 
# with each column right-justified
# assume that inner lists will contain same nr of strings

tabledata = [['apples', 'oranges', 'cherries', 'banana'],
				['Alice', 'Bob', 'Carol', 'david'],
				['dogs', 'cats', 'moose', 'goose']]



def column_width(table): #this function calculates the length of longest of words in the table
	main_list = []
	for x in tabledata:
		for y in x:
			main_list.append((len(y)))
	width = max(main_list)
	#print('length of longest entry: ', width)
	return width

width = column_width(tabledata)

def printtable(table, width):

	num_rows = len(table[0]) #nr of items in any inner list
	num_cols = len(table) #nr of inner lists

	
	for row_index in range(num_rows): # loop through the rows (nr of items in any list)
		for col_index in range(num_cols): # loop through column indexes
			item = table[col_index][row_index] # get the items
			print(item.rjust(width), end=' ') # print justified item making sure it stays on the same line using end =''
		print() # print blank line for next iteration

printtable(tabledata, width)

# Hint: Your code will first have to find the longest string in each of the inner lists so that the whole column 
# can be wide enough to fit all the strings. 

# You can store the maximum width of each column as a list of integers. 

# The printTable() function can begin with colWidths = [0] * len(tableData), 
# which will create a list containing the same number of 0 values as the number of inner lists in tableData. 

# That way, colWidths[0] can store the width of the longest string in tableData[0], 
# colWidths[1] can store the width of the longest string in tableData[1], and so on. 
# You can then find the largest value in the colWidths list to find out what integer width to pass to the rjust() string method.