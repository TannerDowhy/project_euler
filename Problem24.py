def factorial(num):
	if num == 0:
		return 1
	else:
		return num * factorial(num-1)

number = []
numbers = [0,1,2,3,4,5,6,7,8,9]
f = 0
for i in range(9, -1, -1):
	# f = factorial(i)
	idx = 0
	while f < 1000000:
		f += factorial(i)
		idx += 1
	f -= factorial(i)
	number.append(numbers.pop(idx-1))
print(int(''.join([str(x) for x in number])))