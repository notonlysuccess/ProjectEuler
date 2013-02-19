from euler import *
y , m , d = 1900 , 1 , 6
cnt = 0
while y < 2001:
	if y > 1900 and d == 1:
		cnt += 1
	for i in range(7):
		y , m , d = nextDay(y , m , d)
print cnt
