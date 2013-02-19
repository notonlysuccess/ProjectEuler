p = set(n*(3*n - 1) / 2 for n in range(1 , 10000))
for a in p:
	for b in p:
		if a > b and a + b in p and a - b in p:
			print a - b
