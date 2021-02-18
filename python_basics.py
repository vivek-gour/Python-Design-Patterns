"""
GIL

1.    Keywords in Python programming language
        False,	class,	finally,	is,	return
        None,	continue,	for,	lambda,	try,
        True,	def,	from,	nonlocal,	while,
        and,	del,	global,	not,	with,
        as,	elif,	if,	or,	yield,
        assert,	else,	import,	pass,
        break,	except,	in,	raise
        
2. Python Variables.
    A = 1
    A = "ASD"

3. Python Data Types - Mutable and Immutable
        Python Numbers - 1
        Python List - []
        [x*x for x in range(6)]
        Python Tuple - ()
        Python Strings - "" or ''
        Python Set - {} & set()
        Python Dictionary - {key: value}
        {x: x*x for x in range(6)}

        a = []
        isinstance("vivek", str)

4. Python Namespace and Scope

5. if elif else

6. for else

7. while else # The else part is executed if the condition in the while loop evaluates to False

8. break and continue

9. pass

10. function

11. Pass by reference

def test(a):
    a.append(3)


a = [1, 2]
test(a)
print a

12. Func Arguments

13. Python Anonymous/Lambda Function

14. Global variable

def foo():
    x = 20

    def bar():
        global x
        x = 25

    print("Before calling bar: ", x) # it will print 20
    print("Calling bar now")
    bar()
    print("After calling bar: ", x) # it will print 20

foo()
print("x in main : ", x) # it will print 25

15. Module

example.py

16. package
feature:
    __init__.py
    feature.py

17. Class - Multiple and Multi level

18. Operator overloading This feature in Python, that allows same operators to have different meaning according to the
context is called operators overloading
class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x,self.y)

    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x,y)

a = Point(2, 3)
b = Point(4, 2)

print (a + b)

19. Iterator - Iterator in Python is simply an object that can be iterated upon. An object which will return data, one
 element at a time.

20. Generator - with yield we can create any function as generator

a = (x**x for x in [1,2,3,4,5])

here a is also a generator object

21. Closuer Function

def func(msg):
    def func2():
        print(msg)
    return func2

a = func("Vivek Gour")
a()

22. Decorator

def myDeco(func):
    def inner(*args, **kwargs):
        # do something
        print("running before any function")
        return func(*args, **kwargs)
    return inner

23. Python property

class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    def get_temperature(self):
        print("Getting value")
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value

    temperature = property(get_temperature,set_temperature)

c = Celsius()
print c.temperature
c.temperature = 23
print c.temperature
print c.to_fahrenheit()

24. shallow and deep copy

Shallow copy is used when a new instance type gets created and it keeps the values that are copied in the new instance.
Shallow copy is used to copy the reference pointers just like it copies the values. These references point to the original
objects and the changes made in any member of the class will also affect the original copy of it. Shallow copy allows faster
execution of the program and it depends on the size of the data that is used.
Deep copy is used to store the values that are already copied. Deep copy doesnt copy the reference pointers to the objects.
It makes the reference to an object and the new object that is pointed by some other object gets stored. The changes made
in the original copy wont affect any other copy that uses the object. Deep copy makes execution of the program slower due
to making certain copies for each object that is been called.

"""

