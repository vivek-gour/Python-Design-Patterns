# is will return True if two variables point to the same object, == if the objects referred to by the variables are equal.
# >>> a = [1, 2, 3]
# >>> b = a
# >>> b is a
# True
# >>> b == a
# True

# Make a new copy of list `a` via the slice operator,
# and assign it to variable `b`
# >>> b = a[:]
# >>> b is a
# False
# >>> b == a
# True
# In your case, the second test only works because Python caches small integer objects, which is an implementation detail. For larger integers, this does not work:
# >>> 1000 is 10**3
# False
# >>> 1000 == 10**3
# True
# The same holds true for string literals:
# >>> "a" is "a"
# True
# >>> "aa" is "a" * 2
# True
# >>> x = "a"
# >>> "aa" is x * 2
# False
# >>> "aa" is intern(x*2)
# True
