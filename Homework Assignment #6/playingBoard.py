"""
	Homework Assignment #6
	Advanced Loops
	Draw a Playing Board
							"""

"""
Example: 4 X 4 Playing Board

1. 4 X 4 Playing board has four rows and four columns
2. Each row has three columns seperated by four spaces(1 space- Three spaces)
3. There should be a seperator between two adjacent rows
4. Use indeces to build the board
5. Row indeces: Build columns at even indeces and seperators(---) at odd
6. Column indeces: Use vertical bars(|) at multiples of four indeces and spaces at the rest
7. Loop ((rows*2)-1) times using range with initial value at 0 to build rows and 
 (columns*4) times with initial value at 1 to build columns
8. Seperator can be formed by "-"*((columns*4)-1)

  123456789X12345 
0    |   |   | 
1 ---------------
2    |   |   | 
3 ---------------
4    |   |   | 
5 ---------------
6    |   |   | 

"""

def playingBoard(rows, columns):
	# Operating System module
	import os
	# Using built-in function to get dimensions of the terminal window
	try:
		width, height = os.get_terminal_size(0)
	except OSError:
		width, height = os.get_terminal_size(1)

	# Divide height and width by spaces each row and column requires respectively to get the limit values
	rowLimit = int(height/2) 
	columnLimit = int(width/4)

	if rows <= rowLimit and columns <= columnLimit: # Limits are set to avoid wrapping
		for row in range((rows*2)-1): 
			if row % 2 == 0: # Build columns at even rows
				for column in range(1, (columns*4)): # We need to fill up with spaces between vertical lines
					if column % 4 != 0:
						if column != ((columns*4)-1):
							print(" ", end="")
						else:
							print(" ")
					else: # Vertical lines come at multiples of four
						print("|", end="")
			else: # This block is for seperator
				print("-"*((columns*4)-1))
		return True
	else: # When arguments(rows and columns) exceed the limits
		return False

playingBoard(5, 5)