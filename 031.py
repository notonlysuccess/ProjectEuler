coin=[1,2,5,10,20,50,100,200]
dp = [1] + [0] * 200
for c in coin:
	for i in xrange(c , 201):
		dp[i] += dp[i-c]
print dp[200]
