from euler import *
prime = getPrime(11111)
index = 1
while True:
	if (reduce(mul , [v[1]+1 for v in fuckPrime(index * (index + 1) / 2 , prime)]) > 500):
		print index * (index + 1) / 2
		break;
	index += 1
