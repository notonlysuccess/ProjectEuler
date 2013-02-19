num_dict = { 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six",
7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven",
12:"twelve", 13:"thirteen", 14: "fourteen", 15: "fifteen",
16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen",
20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty",
70: "seventy", 80: "eighty", 90: "ninety", 100: "hundred",
1000: "thousand"}

def func(i):
	ret = 0
	if i == 1000:
		ret += len("one") + len("thousand")
	elif i >= 100:
		ret += len(num_dict[i/100]) + len("hundred")
		if i % 100 != 0:
			ret += len("and") + func(i%100)
	elif i >= 20:
		ret += len(num_dict[i - i%10])
		if i % 10 != 0:
			ret += len(num_dict[i%10])
	else:
		ret += len(num_dict[i])
	return ret
print sum(func(i) for i in range(1,1001))
