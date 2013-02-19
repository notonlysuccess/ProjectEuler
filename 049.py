from euler import *
prime = getPrime(10000)
for a in prime:
	for b in prime:
		if a < b and sorted(str(a)) == sorted(str(b)) and b*2 - a in prime and sorted(str(a)) == sorted(str(b*2 - a)):
			print str(a) + str(b) + str(b*2 - a)
