#############################################################
# What is the largest prime factor of the number 600851475143
#############################################################
import math

num = 600851475143 

max_p = 1
for i in range(3, int(math.sqrt(num)) + 1, 2):
	while num % i == 0:
		max_p = i
		num = num / i 

if num > 2:
	max_p = num 

print(max_p)