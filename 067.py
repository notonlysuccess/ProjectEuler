num = []
for line in open("067.in"):
	num += [map(int,line.split(" "))]
for i in xrange(98 , -1 , -1):
	for j in xrange(0 , i+1):
		num[i][j] += max(num[i+1][j] , num[i+1][j+1])
print num[0][0]
