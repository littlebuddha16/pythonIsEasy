"""
	Homework Assignment #7
	Dictionaries and Sets
	Favourite Song
	Author: Kiran Kumar P V
							 """

"""
Function to clear the terminal

1. OS module has functions which can be used to interact with underlying Operating System
2. Use system function to clear the terminal
3. Use os.name and "if block" to clear either Windows terminal or Linux terminal(NT represents Windows OS)
"""
def clear():
	import os
	if os.name == 'nt': 
		os.system('cls')
	else:
		os.system('clear')

"""
Creating a dictionary for my favourite carnatic song

1. Dictionary elements are defined within flower brackets({})
2. Dictionaries have keys and values
3. Key and it's value are seperated by colon(:)
4. Each "key: value" seperated by comma(,)
"""

favouriteSong = { 
	'Song': 'Nagumomu Ganaleni', 
	'Genre': 'Carnatic', 
	'Language': 'Telugu', 
	'Composed By': 'Tyagaraja',
	'Raga': 'Abheri',
	'Artist': 'Tyagaraja',
	'Duration': '6 minutes',
	'Release Date': '1767 - 1847',
	'Best Version': 'Nagumomu Ganaleni by Kartik'
	}

# Sets do not store duplicate values and also they don't keep the order of the elements

attributes = set() # Empty Set
clear() # Clears the terminal
print('*'*5, 'Favourite Song', '*'*5, '\n') # Title

""" 
Add Dictionary keys to empty set

1. Use 'for' loop to iterate through dictionary keys
2. Use add function to add the keys to the set
3. Print key and dictionary value

Example:
Name: Kiran
Age: 28
Country: India
"""

for key in favouriteSong:
	attributes.add(key)
	print(key + ':', favouriteSong[key])

"""
Function for Guessing Game

1. Get the attribute from the User, check in set if the key exists and print appropriate response if it does not
2. If the key does exists then take the answer
3. Check in the dictionary if the value is right and print a response
4. Return False either key is incorrect or value 
"""

def guessGame():
	key = input('Attribute you want to guess(case-sensitive): ') # Read host
	if key in attributes: # Key check
		value = input('Your answer(case-sensitive): ') # Read host
		if favouriteSong[key] == value: # Value check
			print('Correct!') # Response
			return True
		else:
			print('Incorrect!') # Response
			return False
	else:
		print('Attribute does not exist') # Response
		return False

"""
Set the game on loop: Use while to loop the game function and break it based on User's response
"""
while True:
	control = int(input('\nDo you wanna play a "Guessing Game" on my favourite song?(1- yes/0- no): ')) # Read host
	if control != 0: # Runs the game
		clear()
		print('*'*5, 'Guess Key and Value', '*'*5, '\n') # Title
		guessGame()
	else: # Game exit
		break