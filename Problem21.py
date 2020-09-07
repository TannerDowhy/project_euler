import numpy as np

def find_devisors(num):
	arr = np.array([])
	for i in range(1, num//2 + 1):
		if num % i == 0:
			arr = np.append(arr, i)
	return np.sum(arr)

def is_amicable(arr1, arr2):
	s1 = np.sum(arr1)
	s2 = np.sum(arr2)
	return s1, s2

arr = np.zeros(10000)
for i in range(2,10000):
	arr[i] = find_devisors(i)

s = 0
for i in range(2,len(arr)):
	if arr[i] > i:
		if arr[i] < 10000:
			if i == arr[int(arr[i])]:
				s += arr[i]
				s += arr[int(arr[i])]
print(s)