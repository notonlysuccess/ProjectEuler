C = [[0 for i in range(101)] for j in range(101)]
C[0][0] = 1
ret = 0
for i in xrange(1,101):
	for j in xrange(0,i+1):
		if j != 0: C[i][j] += C[i-1][j-1]
		if j != i: C[i][j] += C[i-1][j]
		if C[i][j] > 1000000: ret += 1
print ret
