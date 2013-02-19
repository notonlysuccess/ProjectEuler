fib = [1,1]
limit = 10**999
while True:
	fib.append(fib[-1] + fib[-2])
	if fib[-1] > limit:
		print len(fib)
		break
