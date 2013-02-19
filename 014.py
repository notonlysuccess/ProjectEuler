x = {1:1}
def func(n):
	if not n in x:
		x[n] = func(n * 3 + 1 if n & 1 else n / 2) + 1
	return x[n]
print max(xrange(2, 1000000) , key = func)
