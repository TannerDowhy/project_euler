def find_path(arr):
	for i in range(len(arr)-2,-1, -1):
		for j in range(i, -1, -1):
			arr[i][j] += max(arr[i+1][j], arr[i+1][j+1])
	return arr[0][0]

arr = []
with open("Problem18.txt", 'r') as f:
	for line in f:
		l = line.replace('\n', '')
		l = l.split(" ")
		l = [int(x) for x in l]
		arr.append(l)
	f.close()
print(find_path(arr))

