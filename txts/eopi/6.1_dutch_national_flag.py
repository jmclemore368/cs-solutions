import random
import time

	
	
#=========#
	
	
	
def swap(a, i, j):
	temp = a[i]
	a[i] = a[j]
	a[j] = temp
	
	
	
#=========#
	
	
	
def dnfp_slow(a, idx):
	""" O(n^2) Time & O(1) Space """
	
	pivot = a[idx]
	# First pass: group elements smaller than pivot.
	i = 0
	while i < len(a):
		j = i + 1
		# Look for a smaller element.
		while j < len(a):
			if a[j] < pivot:
				swap(a, i, j)
				break
			j += 1
		i += 1
	
	# Second pass: group elements larger than pivot.
	i = len(a) - 1
	while i >= 0 and a[i] >= pivot:
		j = i - 1
		# Look for a larger element. Stop when we reach an element less
		# than pivot, since first pass has moved them to the start of a.
		while j >= 0 and a[j] >= pivot:
			if a[j] > pivot:
				swap(a, i, j)
				break
			j -= 1
		i -= 1
	
	
	
#=========#
	
	
	
def dnfp_two_pass(a, idx):
	""" O(n) Time & O(1) Space """
	
	pivot = a[idx]

	# First pass: group elements smaller than pivot
	i = 0
	s = 0
	while i < len(a):
		if a[i] < pivot:
			swap(a, i, s)
			s += 1
		i += 1
	
	# Second pass: group elements larger than pivot
	i = len(a) - 1
	g =  len(a) - 1
	while i >= 0 and a[i] >= pivot:
		if a[i] > pivot:
			swap(a, i, g)
			g -= 1
		i -= 1
	
	
	
#=========#
	
	
	
def dnfp_one_pass(a, idx):
	""" O(n) Time & O(1) Space """
	
	pivot = a[idx]
	
	# Keep the following invariants during partitioning:
	# bottom group: a[0:s]
	# middle group: a[s:e]
	# unclassified group: a[e:g]
	# top group: a[g:len(a)]
	
	
	s = 0
	e = 0
	g = len(a)
	
	# Keep iterating as long as there is an unclassified element.
	while e < g:
		# a[e] is the incoming unclassified element.
		if a[e] < pivot:
			swap(a, s, e)
			s += 1
			e += 1
		elif a[e] == pivot:
			e += 1
		else: # a[e] > pivot
			g -= 1
			swap(a, e, g)
	
	
	
#=========#
	
	
	
def rand_list(size):
	l = []
	for i in range(size):
		l.append(random.randrange(0, 10))
	return l
	
	
	
def dnfp_unit_test(dnfp):
	
	for i in range(1000):
	
		size = random.randrange(1, 100)
		a = rand_list(size)
		idx = random.randrange(0, size)
		pivot = a[idx]

		#print "\nBefore: [" + ",".join([str(x) for x in a]) + "]"
		#print "\t Pivot: " + str(a[idx])
		dnfp(a, idx)
		#print "\t After: [" + ",".join([str(x) for x in a]) + "]"
		
		i = 0
		while i < size and a[i] < pivot:
			i += 1
		while i < size and a[i] == pivot:
			i += 1
		while i < size and a[i] > pivot:
			i += 1
			
		assert i == size
		
	
	
#=========#
	
	
	
if __name__ == "__main__":
	dnfp_unit_test(dnfp_slow)
	dnfp_unit_test(dnfp_two_pass)
	dnfp_unit_test(dnfp_one_pass)
	print "Success!"
	
	
	
	

	
	
	
	
