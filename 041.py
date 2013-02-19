from euler import *
for i in range(0,9):
	for p in perm("987654321"[i::]):
		if isPrime(int(p)):
			print p
			exit()
