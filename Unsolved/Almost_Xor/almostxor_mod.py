'''
Convert string to hex
eg. ABCD to 0x41_42_43_44
'''
def to_num(s):
	x = 0
	for i in range(len(s)): x += ord(s[-1-i]) * pow(256, i)
	return x

'''
Convert string to hex of n-bytes

	map(lambda x: hex(x), get_nums("ABCD", 1))
	['0x41', '0x42', '0x43', '0x44']

	map(lambda x: hex(x), get_nums("ABCD", 3))
	['0x414243', '0x440000']
'''
def get_nums(s, n):
	sections = [s[i:i+n] for i in range(0, len(s), n)]
	sections[-1] = sections[-1] + ("\x00" * (n - len(sections[-1])))
	return [to_num(x) for x in sections]

'''
Splits up the value x into bits of n-width
MSB is index-0
'''
def get_vals(x, n):
	vals = []
	mask = (1 << n) - 1 ## get bottom n bits
	# print "Mask:", bin(mask), hex(mask)
	for i in range(8):
		'''
		print "---------------------"
		print "i:", i
		print "x: ", hex(x)
		print "append: ", hex(x & mask)
		'''
		vals.append(x & mask)
		x = x >> n
	# print "vals-original", vals
	vals.reverse()
	# print "vals-reverse", vals
	return vals

'''
SELF
Function to reverse the above to get the original
'''
def reverse_get_vals(list_of_values, n):
	original = 0
	for val in n:
		g <<= n
		g += original;
	return original

'''
Return the original string from the list produced by get_vals()
'''
def get_chrs(val_list, n):
	x = val_list[0]
	chrs = []
	for i in range(1, len(val_list)):
		x <<= n
		x += val_list[i]
	for i in range(n):
		chrs.append(chr(x % 256))
		x //= 256
	chrs.reverse()
	return "".join(chrs)

'''
Add the n-width bits of m and k together and 
ignore carryover bits
Returns the cipher_char
'''
def encr_vals(m_chr, k_chr, n):
	return (m_chr + k_chr) & ((1 << n) - 1)

'''
SELF
Returns the m_char
'''
def decr_vals(c_chr, k_chr, n):
	bit_mask = ((1 << n) - 1)
	diff = c_chr - k_chr
	if (diff < 0):
		diff += (1 << n)
		# add back carry-over bit we lost
	assert diff <= bit_mask
	return diff


def encrypt(k, m, n):
	if (n >= 8): raise ValueError("n is too high!")
	rep_k = k * (len(m) // len(k)) + k[:len(m) % len(k)] # repeated key
	m_val_list = [get_vals(x, n) for x in get_nums(m, n)]
	k_val_list = [get_vals(x, n) for x in get_nums(rep_k, n)]
	m_vals, k_vals, c_vals = [], [], []
	for lst in m_val_list: m_vals += lst ## combine lists together
	for lst in k_val_list: k_vals += lst ## combine lists together
	c_vals = [encr_vals(m_vals[i], k_vals[i % len(k_vals)], n)
		for i in range(0, len(m_vals))]
	c_val_list = [c_vals[i:i+8] for i in range(0, len(c_vals), 8)]
	return "".join([get_chrs(lst, n) for lst in c_val_list])

'''
SELF
Returns the deciphered text
'''
def decrypt(k, m, n):
	if (n >= 8): raise ValueError("n is too high!")
	rep_k = k * (len(m) // len(k)) + k[:len(m) % len(k)] # repeated key
	m_val_list = [get_vals(x, n) for x in get_nums(m, n)]
	k_val_list = [get_vals(x, n) for x in get_nums(rep_k, n)]
	m_vals, k_vals, c_vals = [], [], []
	for lst in m_val_list: m_vals += lst 
	for lst in k_val_list: k_vals += lst 
	c_vals = [decr_vals(m_vals[i], k_vals[i % len(k_vals)], n) ## change to decrypt
		for i in range(0, len(m_vals))]
	c_val_list = [c_vals[i:i+8] for i in range(0, len(c_vals), 8)]
	return "".join([get_chrs(lst, n) for lst in c_val_list])