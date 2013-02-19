for line in open("059.in"):
	l = map(int,line[:-1].split(","))
pw = [103,111,100]
print sum(pw[i%3]^j for i , j in enumerate(l))
	
