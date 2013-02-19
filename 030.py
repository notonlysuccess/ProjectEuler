print sum(x for x in xrange(2,200000) if sum(int(str(x)[i])**5 for i in range(len(str(x)))) == x)
