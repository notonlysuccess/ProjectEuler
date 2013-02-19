n = 1000000 - 1
a = range(10)
ret = []
for i in range(9 , 0 , -1):
	factorial = reduce(lambda x , y: x * y , range(1 , i + 1))
	j = n / factorial
	ret.append(a[j])
	del a[j]
	n = n % factorial
ret.append(a[0])
print ret
