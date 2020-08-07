###########################################################################
# Find the largest palindrome made from the product of two 3-digit numbers.
###########################################################################

def palindrome(prod):
	numList = list(str(prod))
	for i in range(len(numList) // 2):
		if numList[i] != numList[-i-1]:
			return False
	return True

for i in range(100, 1000):
	for j in range(100, 1000):
		product = i * j
		if palindrome(product):
			print(i, j)
			largest = product 

print(largest)