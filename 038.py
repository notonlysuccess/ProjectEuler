for i in range(1 , 10000):
	l = 0
	s = ""
	for j in range(1 , 10):
		l += len(str(i*j))
		s += str(i*j)
		if l > 9: break
		elif l == 9:
			if ''.join(sorted(str(s))) == "123456789":
				print s
			break
