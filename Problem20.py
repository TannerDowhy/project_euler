def factorial(num):
	if num < 2:
		return num
	return num * factorial(num-1)

print(sum([int(x) for x in str(factorial(100))]))
