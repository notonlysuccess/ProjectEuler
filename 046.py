from euler import *
for x in xrange(3,111111111,2):
	if isPrime(x): continue
	flag = True
	for i in xrange(1,11111111):
		t = 2 * i * i
		if t > x: break
		if isPrime(x - t):
			flag = False
			break
	if flag:
		print x
		exit()
