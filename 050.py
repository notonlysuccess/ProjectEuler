from euler import *
prime = getPrime(1000000)
isPrime = getIsPrime(1000000)
ans = 21
for i in xrange(len(prime)):
	if i + ans >= len(prime) or sum(prime[i:i+ans]) >= 1000000: break
	for j in xrange(ans + 1,1000000):
		if i + j >= len(prime):break
		s = sum(prime[i:i+j])
		if s >= 1000000: break
		if isPrime[s]:
			ans = j
			print prime[i] , ans , s
