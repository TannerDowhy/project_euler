import numpy as np

def factors(num):
	i = 2
	factors = np.array([])
	while i <= num:
		if num % i == 0:
			factors = np.append(factors,i)
			num /= i 
		else:
			i += 1
	return factors

i = 0
counter = 1
prod = prod = 0
while prod < 500:
	i += counter 
	counter += 1
	fact = factors(i)
	uniques = np.unique(fact, return_counts=True)

	prod = 1
	for item in uniques[1]:
		prod *= (item+1)

print(i)

