sum = 1
for i in xrange(3 , 1002 , 2):
	r = i**2
	for j in xrange(4):
		sum += r - j * (i - 1)
print sum
