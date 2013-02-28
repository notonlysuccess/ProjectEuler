N = 10
M = 10**12
a = {}
b = {}
totalState = 0
for i in range(0 , N * 2 + 1):
	for j in range(0 , N * 2 + 1 - i):
		a[(i , j , N * 2 - i - j)] = totalState
		b[totalState] = (i , j , N * 2 - i - j)
		totalState += 1

init = [[0 for j in range(totalState*2)] for i in range(totalState*2)]
