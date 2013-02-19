from euler import *
print sum(x for x in xrange(1000000) if str(x) == str(x)[::-1] and dec2bin(str(x)) == dec2bin(str(x))[::-1])
