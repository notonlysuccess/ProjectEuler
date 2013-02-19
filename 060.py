from euler import *
prime = getPrime(10000)
def pps(pp , i):
	if len(pp) == 5:
		print pp , sum(pp)
		exit()
	for j in xrange(i,len(prime)):
		p = prime[j]
		for x in pp:
			if not isPrime(int(str(x)+str(p))) or not isPrime(int(str(p)+str(x))):
				break
		else:
			 pps(pp+[p] , j + 1)
pps([] , 0)
