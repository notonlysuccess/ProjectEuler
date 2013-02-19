s = ""
for i in xrange(300000):s += str(i)
print reduce(lambda x,y:x*y ,[int(s[10**x]) for x in range(7)])
