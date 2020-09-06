import numpy as np 
import pdb

cache = np.zeros(1000000)
for i in range(3, 1000000):
	counter = 0
	start = i 
	while i > 1:
		if i < start:
			cache[start] = cache[int(i)] + counter
			break
		if i%2 == 0:
			i = i/2
			counter += 1
		else:
			i = 3*i + 1
			counter += 1

print(np.where(cache == np.amax(cache)), np.amax(cache))