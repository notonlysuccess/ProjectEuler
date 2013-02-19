p = [0] * 1001
for a in xrange(1 , 1000):
	for b in xrange(a , 1000):
		c = (a**2 + b**2) ** 0.5
		if a + b + c > 1000:
			break
		if c % 1 == 0:
			p[a+b+int(c)] += 1
print max((p[i] , i) for i in xrange(len(p)))
