from euler import *
prime = getPrime(11111)
for i in xrange(2 , 11111111):
	if all(len(fuckPrime(j , prime)) == 4 for j in xrange(i , i + 4)):
		print i
		break

