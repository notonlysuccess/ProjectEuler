from euler import *
def rotation(n):
	s = str(n)
	return (int(s[i:]+s[:i]) for i in xrange(len(s)))
prime = set(getPrime(1000000))
print sum(all(r in prime for r in rotation(p)) for p in prime)
