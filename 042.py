tri = set(i*(i+1)/2 for i in range(1 , 100))
for line in open("042.in"):
	l = line.split(',')
cnt = 0
for line in l:
	if sum(map(lambda x:ord(x) - ord('A') + 1,[c for c in list(line) if c.isalpha()])) in tri:
		cnt += 1
print cnt
