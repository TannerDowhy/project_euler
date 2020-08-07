# What is the smallest positive number that is evenly 
# divisible by all of the numbers from 1 to 20?

def divisible(mini):
	# if mini % 2 != 0:
	# 	mini += 1
	# 	break
	print(mini)
	for i in range(3, 21):
		print(i)
		if mini % i == 0:
			if i == 20:
				num = mini
				return num
		else:
			print('hi')
			return None

mini = 20
num = None
while(num == None):
	num = divisible(mini)
	mini += 2
print(num)