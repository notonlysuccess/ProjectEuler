def root(n , c , m , a):
	c -= a * m
	m = (n - c*c)/m
	return -c , m
ans = 0
for n in range(2,10001):
	c , m = 0 , 1 
	mp = {}
	for i in xrange(10000):
		a = (n**0.5 + c)/m
		if a % 1 == 0: 
			break
		c , m = root(n , c , m , int(a))
		if mp.get((c,m)):
			ans += (i - mp[(c,m)])%2
			break
		else:
			mp[(c,m)] = i
print ans
