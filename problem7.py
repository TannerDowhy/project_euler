def is_prime(n):
	for i in range(2,(n//2)+1):
		if n % i == 0:
			return False
	return True

def nth_prime(n):
	num = 3
	prime = 2
	while prime < n:
		num += 2
		if is_prime(num):
			prime += 1
	return num

print(nth_prime(10001))