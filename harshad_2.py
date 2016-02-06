#!/usr/bin/env python3
""" Harshad Number Problem """
__author__ = "Rohan Pandit"

def is_harshad(n):

    if n % sum_digits(n) == 0 :
		return True
	else:
		return False

def sum_digits(n):
	return sum(map(int, str(n)))

def main():
	assert(is_harshad(11) == False)
	assert(is_harshad(12) == True)
	assert(is_harshad(5) == True)

if __name__ == "__main__":
	main()
