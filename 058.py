from euler import *
c , t , x = 0 , 1 , 1
for i in xrange(2,1000000,2):
	for j in xrange(4):
		x += i
		if isPrime(x):
			c += 1
	t += 4
	if c * 10 < t:
		print i + 1
		break

