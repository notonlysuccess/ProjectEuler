for x in xrange(2,100000000):
	xx = x*x - 1
	if xx % 61 == 0:
		xx /= 61
		if xx ** 0.5 % 1 == 0:
			print xx**0.5
exit()
sq = [x*x for x in xrange(1,1000000)]
for d in range(107 , 1001):
	if (d ** 0.5) % 1 == 0: continue
	for s in sq:
		ss = s * d + 1
		if (ss ** 0.5) % 1 == 0:
			print d , ss
			break
	else:
		print d
		break

