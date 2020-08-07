##########################################################
# By considering the terms in the Fibonacci sequence whose 
# values do not exceed four million, find the sum of the 
# even-valued terms.
##########################################################

num = 1
prev = 1
sum = 0

while(True):
	if num > 4000000:
		break
	new = num + prev
	prev = num
	num = new
	if new % 2 == 0:
		sum += new

print(sum)