# map function


def myLambda(x):
    print x
    return x * x


print map(lambda x: x * x, {"one": 1, "two": 2}.values())

# reduce function

print reduce(lambda x, y: x + y + x, [1, 2, 3, 4], 0)
print (((2 + 2) + 4 + 3) + 11 + 4)

print reduce(lambda x, y: x + y + x, [1, 2, 3, 4], 1)
print ((((1 + 1 + 1) + 3 + 2) + 8 + 3) + 19 + 4)

print reduce(lambda x, y: x + y + x, [1, 2, 3, 4], 2)
print ((((2 + 1 + 2) + 5 + 2) + 12 + 3) + 27 + 4)

# filter function

print filter(lambda x: x if x else None, [0, '', None, True, 1])
print filter(lambda x: x is True, [0, '', None, True, 1])