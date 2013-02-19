for x in xrange(1,10000000):
	for i in xrange(2 , 7):
		if sorted(str(x*i)) != sorted(str(x)):
			break
	else:
		print x
		break
