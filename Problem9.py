def check_pythagoras(a,b,c):
	if (a**2) + (b**2) == (c**2):
		return True
	else:
		return False

def check_sum(a,b,c):
	if a+b+c == 1000:
		return True
	else:
		return False 

def driver():
	for i in range(0,1000):
		for j in range(i+1, 1000):
			for k in range(j+1, 1000):
				if check_pythagoras(i,j,k) and check_sum(i,j,k):
					return i*j*k

print(driver())