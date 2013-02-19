A = [[] for i in range(9)]
for i in xrange(3,9):
	for n in xrange(10000):
		p = n * ((i-2) * n - (i - 4))/2
		if p >= 10000: break
		if p >= 1000: A[i].append(p)
def dfs(X,A):
	if len(X) == 6:
		if X[-1] % 100 == X[0] / 100:
			print sum(X)
			print X
			exit()
	for a in A:
		for x in a:
			if len(X) == 0 or X[-1] % 100 == x / 100:
				dfs(X+[x],[b for b in A if b != a])
dfs([],A)
