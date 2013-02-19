mp = {}
for i in xrange(10000):
	x = i**3
	y = ''.join(sorted(str(x)))
	if mp.get(y):
		mp[y][1] += 1
		if mp[y][1] == 5:
			print mp[y][0]
			break
	else:
		mp[y] = [x , 1]
