n = 28124
d = [0] * n
for i in range(1 , n):
	for j in range(2*i , n , i):
		d[j] += i
ret , ab = 0 , set()
for i in xrange(1 , n):
	if d[i] > i: ab.add(i)
	if all(not i - j in ab for j in ab): ret += i
print ret
