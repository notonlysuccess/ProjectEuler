from euler import *
prime = [1,2,3,5,7,11,13,17]
s = "0123456789"
ret = 0
for p in perm(s):
	if all(int(p[j:j+3]) % prime[j] == 0 for j in range(1,8)):
		ret += int(p)
print ret
