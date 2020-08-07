#####################################################
# What is the smallest positive number that is evenly 
# divisible by all of the numbers from 1 to 20?
#####################################################

def divisible(mini):
	for i in range(5, 21):
		if mini % i == 0:
			if i == 20:
				num = mini
				return num
		else:
			return None

mini = 20
num = None
while(num == None):
	num = divisible(mini)
	mini += 10
print(num)