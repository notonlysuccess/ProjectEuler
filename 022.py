for line in open("022.in"):
	l = line.split(',')
ret = 0
for index, line in enumerate(sorted(l)):
	ret += (index + 1) * sum(map(lambda x:ord(x) - ord('A') + 1,[c for c in list(line) if c.isalpha()]))
print ret


