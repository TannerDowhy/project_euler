def num_to_word(num):
	singles = [None, "one","two","three","four","five","six", "seven", "eight", "nine","ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
	tens    = [None, None, "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

	if num < 20:
		return singles[num]
	elif num >= 20 and num <= 90 and num % 10 == 0:
		return tens[num//10]
	elif num > 20 and num < 100:
		return tens[num//10] + singles[num%10]
	elif num >= 100 and num <= 900 and num % 100 == 0:
		return singles[num//100] + "hundred"
	elif num > 100 and num < 1000:
		return singles[num//100] + "hundredand" + num_to_word(num%100)
	elif num == 1000:
		return "onethousand"

count = 0
for i in range(1,1001):
	count += len(num_to_word(i))
print(count)