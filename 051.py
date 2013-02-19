from euler import *
prime = getPrime(100000000)
isPrime = getIsPrime(100000000)
print "ok"
for p in prime:
	sp = str(p)
	for i in xrange(3):
		if str(i) in sp:
			cnt = 0
			for j in xrange(i + 1 , 10):
				if isPrime[int(sp.replace(str(i),str(j)))]:
					cnt += 1
			if cnt >= 7:
				print cnt , p
				exit()
