"""
	Homework Assignment #5
	Basic Loops
	Fizz Buzz Programming Challenge
									"""
# Function to check Prime numbers

def isPrime(integer):
	if integer == 0 or integer == 1: # 0 and 1 are not prime numbers, zero has infinite divisors and one has only one divisor
		return False
	elif integer == 2: # 2 is the only even prime number
		return True
	else:
		# if an integer is not divisible by none of the numbers in the set [2, integer) then it's a prime number
		for i in range(2, integer):
			if integer % i == 0:
				return False
		return True

# Function to address FizzBuzz challenge

def fizzBuzzPrime(num):
	if num % 3 == 0 and num % 5 == 0: # A Number which is a multiple of both 3 and 5 is a FizzBuzz
		print('FizzBuzz')
	elif num % 3 == 0: # Fizz refers to a number that's a multiple of 3
		print('Fizz')
	elif num % 5 == 0: # And Buzz numbers are multiples of 5
		print('Buzz')
	else:
		if isPrime(num):
			print('Prime')
		else:
			print(num)

for number in range(1, 101):
	fizzBuzzPrime(number)
