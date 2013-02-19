from euler import *
a = {0:(0,5,6) , 1:(1,6,7) , 2:(2,7,8) , 3:(3,8,9) , 4:(4,9,5)}
b = {0: (0,), 1: (1,), 2: (2,), 3: (3,), 4: (4,), 5: (0, 4), 6: (0, 1), 7: (1, 2), 8: (2, 3), 9: (3, 4)}
asd = str("123")
for d in perm(range(1,11)):
	c = [0] * 5
	for k , v in b.items():
		for j in v:
			c[j] += d[k]
	if same(c):
		ans = ""
		s = [[d[vv] for vv in v] for k , v in a.items()]
		index = min((s[i][0] , i) for i in range(5))[1]
		ans = ""
		for ss in s[index::1]:
			for sss in ss:
				ans += str(sss)

		for ss in s[:index:1]:
			for sss in ss:
				ans += str(sss)
		print ans
		if len(ans) == 16:
			print ans
