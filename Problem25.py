a = 1
b = 1

offset = 1

while len(str(b)) != 1000:
	tmp = b
	b = a+b
	a = tmp
	offset += 1
print(offset+1)