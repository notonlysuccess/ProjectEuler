t = set(n*(n+1)/2 for n in range(1 , 100000))
p = set(n*(3*n-1)/2 for n in range(1 , 100000))
h = set(n*(2*n-1) for n in range(1,100000))
for tt in t:
	if tt in p and tt in h:
		print tt
