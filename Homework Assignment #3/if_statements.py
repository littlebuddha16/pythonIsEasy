"""
	Homework Assignment #3
	"if" Statements
	Equality
							"""

# Below function returns either True if any two or all of the three elements are equal or false if none of them are equal
def Equality(a, b, c):
	if int(a) == int(b) or int(b) == int(c) or int(c) == int(a):
		return True
	else:
		return False