# https://github.com/adnanaziz/epicode/blob/master/java/src/main/java/com/epi/Parity1.java
# https://github.com/adnanaziz/epicode/blob/master/java/src/main/java/com/epi/Parity2.java
# https://github.com/adnanaziz/epicode/blob/master/java/src/main/java/com/epi/Parity3.java
# https://github.com/adnanaziz/epicode/blob/master/java/src/main/java/com/epi/Parity4.java
	
	
def parity_bit_by_bit(x):
	"""Page 46"""
	result = 0
	while x != 0:
		result ^= (x & 1)
		x >>= 1
	return result
	
	
def parity_bit_by_bit_smart(x):
	"""Page 46"""
	result = 0
	while x != 0:
		result ^= 1
		x &= (x - 1)  # Drops the lowest set bit of x
	return result
	
	
def parity_table(x):
	"""Page 47"""
	word_size = 16
	bit_mask = 0xFFFF
	return (  precomputed_parity[(x >> (3 * word_size)) & bit_mask]
		^ precomputed_parity[(x >> (2 * word_size)) & bit_mask]
		^ precomputed_parity[(x >> (1 * word_size)) & bit_mask]
		^ precomputed_parity[(x >> (0 * word_size)) & bit_mask])
	
	
def parity_assoc(x):
	"""Page 47"""
	x ^= x >> 32
	x ^= x >> 16
	x ^= x >> 8
	x ^= x >> 4
	x ^= x >> 2
	x ^= x >> 1
	return x & 0x1
	
	
