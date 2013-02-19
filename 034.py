f=[1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
print sum(x for x in xrange(10,100000) if reduce(lambda a,b:a+b, [f[int(i)] for i in list(str(x))]) == x)
