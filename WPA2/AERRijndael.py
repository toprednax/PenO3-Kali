a = [0, 0, 0, 0]
b = [0, 0, 0, 0]
h = 0

r = [int("db", 16), int("13", 16), int("53", 16), int("45", 16)]

for i in range(4):
    a[i] = r[i]

    h = r[i] >> 7

    b[i] = r[i] << 1

    b[i] ^= (0x1b & h)

r[0] = hex(b[0] ^ a[3] ^ a[2] ^ b[1] ^ a[1])
r[1] = hex(b[1] ^ a[0] ^ a[3] ^ b[2] ^ a[2])
r[2] = hex(b[2] ^ a[1] ^ a[0] ^ b[3] ^ a[3])
r[3] = hex(b[3] ^ a[2] ^ a[1] ^ b[0] ^ a[0])


print(r)
