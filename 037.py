from euler import *
prime = set(getPrime(1000000))
sum = 0;
for p in prime:
	sp = str(p)
	if p > 10 and all(int(sp[:j:]) in prime and int(sp[j::]) in prime for j in xrange(1 , len(sp))):
		sum += p
print sum
