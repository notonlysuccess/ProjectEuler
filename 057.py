a , b , c = 1 , 1 , 0
for i in xrange(1000):
	a , b = a + b + b , a + b
	if len(str(a)) > len(str(b)):
		c += 1
print c
