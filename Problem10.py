def sieve_of_e(n):
	multiples = set()
	for i in range(2,n):
		if i not in multiples:
			yield i 
			multiples.update(range(i*i, n+1, i))

print(sum(sieve_of_e(2000000)))