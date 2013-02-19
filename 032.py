s = set()
for a in range(2 , 10000):
	for b in range(2 , a):
		c = a * b
		l = sum(map(lambda x:len(str(x)) , [a,b,c]))
		if l > 9: break
		elif l == 9:
			ss = set(str(a)+str(b)+str(c))
			if len(ss) == 9 and not '0' in ss:
				s.add(c)
print sum(x for x in s)
