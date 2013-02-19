x = [[0] * 22] * 22
x[0][1] = 1
for i in xrange(1 , 22):
	for j in xrange(1 , 22):
		x[i][j] = x[i-1][j] + x[i][j-1]
print x[21][21]
