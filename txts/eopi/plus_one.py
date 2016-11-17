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
