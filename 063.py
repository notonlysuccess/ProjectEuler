print len([a for a in xrange(1,10) for b in xrange(100) if len(str(a**b)) == b])
