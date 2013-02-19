from euler import add
print reduce(add , range(101))**2 - sum(x*x for x in range(101))
