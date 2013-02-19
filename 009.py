print max(a*b*(1000-a-b) for a in range(1000) for b in range(1000-a) if a*a+b*b==(1000-a-b)*(1000-a-b))
