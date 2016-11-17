# https://github.com/adnanaziz/epicode/blob/master/java/src/main/java/com/epi/InterconvertingStringInteger.java
	
	
def int_to_string(x):
	"""Page 95"""
	is_negative = False
	if x < 0:
		is_negative = True
		x *= -1  # Be careful for negatives. I.e., -315/10 = -32
	
	s = []
	while True:
		s.append(str(x % 10))
		x /= 10
		if x == 0:
			break
			
	if is_negative:
		s.append('-') # Adds the negative sign back
	s.reverse()
	return ''.join(s)
	
	
def string_to_int(s):
	"""Page 95"""
	i = 1 if s[0] == '-' else 0
	result = 0
	while i < len(s):
		digit = int(s[i])	# I.e., s.charAt(i) - '0' in Java
		result = result * 10 + digit
		i += 1
	return -result if s[0] == '-' else result
	
	
