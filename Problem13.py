s = 0
with open("./Problem13.txt", 'r') as f:
	for line in f:
		s += int(line)
	f.close()

print(str(s)[:10])