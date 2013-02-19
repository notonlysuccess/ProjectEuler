e = [2]
for k in range(1,100):
	e += [1 , k*2 , 1]
a , b = 1 , e[99]
for f in e[98::-1]:
	a , b = b , a + f * b
print sum(map(int,str(b)))
