#!/usr/bin/env python
import random
import sys
	
	
def plus_one(a):
	""" O(n) Time & O(1) Space """
	n = len(a) - 1
	a[n] = a[n] + 1
	i = n
	while i > 0 and a[i] == 10:
		a[i] = 0
		a[i - 1] = a[i - 1] + 1
		i -= 1
		
	if a[0] == 10:
		# Need additional digit as the most significant digit (i.e., a[0])
		# has a carry-out
		a[0] = 0
		a.insert(0, 1)
	return a
	
	
def small_test():
	a = plus_one([9, 9])
	assert len(a) == 3 and a[0] == 1 and a[1] == 0 and a[2] == 0
	
	a = plus_one([3, 1, 4])
	assert len(a) == 3 and a[0] == 3 and a[1] == 1 and a[2] == 5
	
	
def plus_one_unit_test(test):
	""" Test a random list """
	for i in range(1000):
		n = random.randrange(1, 12)
		a = rand_list(n)
		a_dup = list(a)
		
		a = test(a)
		
		if not check(a, a_dup, test):
			sys.exit(0)
			
	print "All tests passed for " + test.__name__
	
	
def rand_list(length):
	a = []
	
	# Make sure first digit is not 0
	a.append(random.randrange(1,10)) 
	length -= 1
	
	for i in range(length):
		a.append(random.randrange(0,10))
		
	return a
	
	
def check(a, a_dup, test):
	# Convert a to number
	a_num = 0
	for n in a:
		a_num = a_num * 10 + n

	# Convert a_dup to number
	a_dup_num = 0
	for n in a_dup:
		a_dup_num = a_dup_num * 10 + n
	
	if not a_num == a_dup_num + 1:
		print "\nError with function: " + test.__name__
		print "Before: [" + ",".join([str(x) for x in a_dup]) + "] -> " + str(a_dup_num)
		print "\tAfter: [" + ",".join([str(x) for x in a]) + "] -> " + str(a_num)
		sys.exit(0)
		
	return True
	
	
if __name__ == "__main__":
	small_test()
	plus_one_unit_test(plus_one)
