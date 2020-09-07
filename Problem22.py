import csv

names = []
with open("Problem22.txt", newline='') as f:
	reader = csv.reader(f, delimiter=',')
	for row in reader:
		for item in row:
			names.append(item)
	f.close()

names = sorted(names)

s = 0
for idx, item in enumerate(names):
	# print(idx,item)
	lsum = 0
	for letter in item:
		lsum += (ord(letter) - 64)
		# print(lsum)
	s += (lsum * (idx + 1))

print(s)
