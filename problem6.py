# Find the difference between the sum of the squares of 
# the first one hundred natural numbers and the square of the sum.

n = 101
sum = 0
sqSum = 0
for i in range(n):
	sum += i
	sqSum += (i ** 2)
sum = sum ** 2

print(sum - sqSum)
