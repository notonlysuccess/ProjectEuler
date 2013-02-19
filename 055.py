cnt = 0
for x in xrange(1,10000):
	for j in xrange(50):
		x = x + int(str(x)[::-1])
		if x == int(str(x)[::-1]):
			cnt += 1
			break
print 9999 - cnt
