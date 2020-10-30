def algoInv(num_1, num_b):
    if int(num_2, 2) == 2:
		num_1 = twee(num_1)
	elif int(num_2, 2) == 3:
		num_1 = drie(num_1)
	else:
		num_1 = make8(num_1[2:])
	
	return num_1



gInv = [["11", "13", "9", "14"], ["14", "11", "13", "9"], ["9", "14", "11", "13"], ["13", "9", "14", "11"]]
b = ["8e", "4d", "a1", "bc"]

for i in range(len(g[1])):
	n1 = algo(bin(int(b[0], 16)), bin(int(g[i][0], 16)))
	n2 = algo(bin(int(b[1], 16)), bin(int(g[i][1], 16)))
	n3 = algo(bin(int(b[2], 16)), bin(int(g[i][2], 16)))
	n4 = algo(bin(int(b[3], 16)), bin(int(g[i][3], 16)))

	n = int(n1, 2) ^ int(n2, 2) ^ int(n3, 2) ^ int(n4, 2)
	print(hex(n)[2:])