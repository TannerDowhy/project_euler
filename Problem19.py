# def count_months(start, end, start_day): 
# 	counter = 0
# 	for i in range(start, end+1):
# 		month_counter = 1
# 		while month_counter < 13:
# 			if month_counter in [1,3,5,7,8,10,12]:
# 				counter, start_day = count_sundays(start_day, 31, counter)
# 				month_counter += 1
# 			elif month_counter in [4,6,9,11]:
# 				counter, start_day = count_sundays(start_day, 30, counter)
# 				month_counter += 1
# 			else:
# 				if i % 4 != 0:
# 					counter, start_day = count_sundays(start_day, 28, counter)
# 				elif (i%4 == 0 and i%100 != 0) or i%400 == 0:
# 					counter, start_day = count_sundays(start_day, 29, counter)
# 				month_counter += 1
# 	return counter

# def count_sundays(start_day, month_days, counter):
# 	for i in range(month_days):
# 		if start_day == 7:
# 			counter += 1
# 			start_day = 1
# 		else:
# 			start_day += 1
# 	return counter, start_day

def count_sundays(start, end, start_day): 
	counter = 0
	for i in range(start, end+1):
		month_counter = 1
		while month_counter < 13:
			if start_day == 7:
				counter += 1
			if month_counter in [1,3,5,7,8,10,12]:
				month_counter += 1
				start_day = (31 % 7) + start_day
			elif month_counter in [4,6,9,11]:
				month_counter += 1
				start_day = (30 % 7) + start_day
			else:
				if i % 4 != 0:
					start_day = (28 % 7) + start_day
				elif (i%4 == 0 and i%100 != 0) or i%400 == 0:
					start_day = (29 % 7) + start_day
				month_counter += 1
			if start_day > 7:
				start_day = start_day % 7
	return counter

print(count_sundays(1901, 2000, 3))
#Tuesday start