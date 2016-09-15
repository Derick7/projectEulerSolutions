limit = 100
sumSquared = reduce(lambda x, y : x+y, [x for x in range(1,limit + 1)])**2
squaredSum = reduce(lambda x, y : x+y, [x**2 for x in range(1,limit + 1)])
print sumSquared - squaredSum
