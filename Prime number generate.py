#!/usr/bin/python
import sys

def sieve(n):
	np1 = n + 1
	# create a list of value from 0 to n (inclusive)
	s = list(range(np1))
	print(s)
	s[1] = 0
	# square n
	sqrtn = int(round(n**0.5))
	for i in range(2, sqrtn + 1):
		if s[i]:
			# mark index divisable by i (from 2 to square of n)
			s[i*i: np1: i] = [0] * len(range(i*i, np1, i))
			print(s[i*i: np1: i])
			print(s)
	# return s with value different 0
	return filter(None, s)

try:
	# get first agurment from command line
	n = int(sys.argv[1])

	# print out the length of a list from function sieve
	print(len(list(sieve(n))))
except ValueError:
	print("Please enter an integer.")