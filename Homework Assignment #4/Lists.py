"""
	Homework Assignment #4
	Lists
	Add unique elements to list
								"""

myUniqueList = [] # New unique elements will be added to this list
myLeftovers = [] # Duplicate of existing elements of myUniqueList will be added here

def addToList(member):
	if member not in myUniqueList: # Adds unique elements to myUniqueList and returns True
		myUniqueList.append(member)
		return True
	else:
		myLeftovers.append(member) # Rejected elements will be added to myLeftovers and returns False
		return False

# Let's add elements

addToList(3)
addToList('littleBuddha')
addToList(None)
addToList(3)
addToList(None)
addToList([])
addToList('Yogi')
addToList(True)
addToList(False)
addToList('Yogi')
addToList('1')
addToList([])
addToList(True)

# Results

print('myUniqueList:', myUniqueList)
print('myLeftovers:', myLeftovers)
