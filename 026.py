def f(x):
	n = 10
	mp = {}
	for i in xrange(2000):
		if n in mp:
			return i - mp[n]
		mp[n] = i;
		n = 10 * (n % x)
print max((f(i) , i) for i in xrange(1 , 1000))[1]
