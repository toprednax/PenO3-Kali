def algo(unencrypted_vector):
	s = [0x0, 0x0, 0x0, 0x0]
	a = unencrypted_vector

	g = [[0x2, 0x3, 0x1, 0x1], 
		[0x1, 0x2, 0x3, 0x1], 
		[0x1, 0x1, 0x2, 0x3], 
		[0x3, 0x1, 0x1, 0x2]]

	num_1 = 0x0

	for i in range(len(g)):
		for j in range(len(a)):
			deg_polynomial = g[j][i]

			if deg_polynomial == 0x2:
				x = two(a[j])
			elif deg_polynomial == 0x3:
				x = three(a[j])
			else:
				x = make8(a[j])
			
			num_1 ^= x
		
		s[i] = num_1
	
	return s

def three(num):
	return two(num) ^ num

def two(num):
	num = make8(num)

	if bin(num)[2:][0] == '0':
		return a * 2

	num = leftshift(num)
	num = make8(num)

	return num ^ 0b00011011			#	Rijndeal polynomial

def leftshift(num):
	return num << 1

def make8(num):
	num = bin(num)[2:]

	if len(num) > 8:
		while len(num) != 8:
			num = num[1:]
		
		return int(num, 2)
	elif len(num) == 8:
		return int(num, 2)
	else:
		while len(num) != 8:
			num = '0' + num
		
		return int(num, 2)

"""
a = [0xdb, 0x13, 0x53, 0x45]

for i in range(len(g[1])):
	n1 = algo(bin(int(a[0], 16)), bin(int(g[i][0], 16)))
	n2 = algo(bin(int(a[1], 16)), bin(int(g[i][1], 16)))
	n3 = algo(bin(int(a[2], 16)), bin(int(g[i][2], 16)))
	n4 = algo(bin(int(a[3], 16)), bin(int(g[i][3], 16)))

	n = int(n1, 2) ^ int(n2, 2) ^ int(n3, 2) ^ int(n4, 2)
	print(hex(n)[2:])
"""