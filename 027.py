from euler import *
isPrime = getIsPrime(1000000)
ret , m = 0 , 0
for a in xrange(-999,1000):
	for b in xrange(-999,1000):
		for i in xrange(1111):
			if i > m:
				m = i
				ret = a * b
			if i*i + a*i + b < 0 or not isPrime[i*i + a * i + b]:
				break
print ret
