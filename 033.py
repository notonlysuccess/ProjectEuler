z , m = 1 , 1
for a in range(11,100): 
	if a % 10:
		for b in range(11 , a): 
			if b % 10:
				a0 , a1 = divmod(a , 10)
				b0 , b1 = divmod(b , 10)
				if (a1 == b0 and b * a0 == a * b1) or (a0 == b1 and b * a1 == a * b0):
					z *= b
					m *= a
from euler import gcd
print m / gcd(z , m)
