__author__ = 'Vivek Gour'
__copyright__ = 'Copyright 2018, Vivek Gour'
__version__ = '1.0.0'
__maintainer__ = 'Vivek Gour'
__email__ = 'Viv30ek@gmail.com'
__status__ = 'Learning'

"""
Once you start using python, there is no escaping from this word self. It is seen in method definitions and in variable
initialization. But getting the idea behind it seems somewhat troublesome. Hopefully at the end of this you will get an
intuitive idea of what self is and where you should use it.

But before talking about the self keyword (which is actually not a python keyword or any special literal), first lets
recall what are class variables and instance variables. Class variables are variables that are being shared with all
instances (objects) which were created using that particular class. So when accessed a class variable from any instance,
the value will be same. Instance variables on the other hand are variables, which all instances keep for themselves
(i.e a particular object owns its instance variables). So typically values of instance variables differ from instance
to instance.

Class variables in python are defined just after the class definition and outside of any methods:

Class SomeClass:
    variable_1 = 'This is a class variable'
    variable_2 = 100   #this is also a class variable
Unlike class variables, instance variables should be defined within methods:

"""


class SomeClass:
    variable_1 = 'This is a class variable'
    variable_2 = 100  # this is also a class variable.

    def __init__(self, param1, param2):
        self.instance_var1 = param1
        # instance_var1 is a instance variable
        self.instance_var2 = param2
        # instance_var2 is a instance variable


# Lets instantiate above class and do some intro-spections about those instances and above class:

obj1 = SomeClass("some thing", 18)
# creating instance of SomeClass named obj1
obj2 = SomeClass(28, 6)
# creating a instance of SomeClass named obj2


print(obj1.variable_1)
'a class variable'

print(obj2.variable_1)
'a class variable'

"""
So ass seen in above, both obj1 and obj2 gives the same value when variable_1 is accessed, which is the normal behaviour
that we should expect from a class variable. Lets find about instance variables:

obj1.instance_var1
'some thing'
obj2.instance_var1
28
So the expected behaviour of instance variables can be seen in above without any error. That is, both obj1 and obj2 have
two different instance variables for themselves.

Instance and class methods in python
Just as there are instance and class variables, there are instance and class methods. These are intended to set or get
status of the relevant class or instance. So purpose of the class methods are to set or get the details (status) of the
class. Purpose of instance methods are to set or get details about instances (objects). Being said that, lets see how to
create instance and class methods in python.

When defining an instance method, the first parameter of the method should always be self. Why it should always be self
is discussed in the next section (which is the main aim of this post). However one can name it anything other than self,
but what that parameter represents will always be the same. And its a good idea for sticking with self as its the
convention.
"""


class SomeClass:
    def create_arr(self):  # An instance method
        self.arr = []

    def insert_to_arr(self, value):  # An instance method
        self.arr.append(value)


"""
We can instantiate above
class as obj3, and do some investigations as follows:
"""

obj3 = SomeClass()
obj3.create_arr()
obj3.insert_to_arr(5)
obj3.arr

"""
[5]
So as you can notice from above, although when defining an instance method the first parameter is self, when calling
that method, we do not pass anything for self as arguments. How come this does not give errors? Whats going on behind
the scene? These are explained in the next section.

Ok, with instance methods explained, all we have left is class methods (so I say). Just like instance methods, in
class methods also there is a special parameter that should be placed as the first parameter. It is the cls parameter,
which represents the class:
"""


class SomeClass:
    def create_arr(self):  # An instance method
        self.arr = []

    def insert_to_arr(self, value):  # An instance method
        self.arr.append(value)

    @classmethod
    def class_method(cls):
        print("the class method was called")


"""
Without even instantiating an object, we can access class methods as follows:

SomeClass.class_method()
So all we have to call the class method with the name of the class. And in here also just like instance methods,
although there is a parameter defined as cls, we do not pass any argument when calling the method - explained next.

Note: Python has another type of methods known as static methods. These are normal methods which do not have any
special parameter as with instance methods or class methods. Therefore these static methods can neither modify
object state nor class state.

Now with all things are being reminded (instance/class variables and methods), lets talk about the use of self
in python (-finally).
"""
"""
self _intuition
Some of you may have got it by now, or some may have got it partially, anyway, the self in python
represents or points the instance which it was called. Lets clarify this with an example
"""


class SomeClass():
    def __init__(self):
        self.arr = []
        # All SomeClass objects will have an array arr by default

    def insert_to_arr(self, value):
        self.arr.append(value)


# So now lets create two objects of SomeClass and append some values for their arrays:

obj1 = SomeClass()
obj2 = SomeClass()
obj1.insert_to_arr(6)

"""
Important: Unlike some other languages, when a new object is created in python, it does not create a new set
of instance methods to itself. So instance methods lie within the class object without being created with each
object initialization nice way to save up memory. Recall that python is a fully object oriented language and
so a class is also an object. So it lives within the memory.
Being said that, lets look at above example. There we have created obj1 and are calling the instance method
insert_to_arr() of SomeClass while passing an argument 6. But now how does that method know "which object is
calling me and whose instance attributes should be updated". Here, to whose arr array should I append the
value 6? Ok, now I think you got it. Thats the job of self. Behind the scene, in every instance method call,
python sends the instance also with that method call. So what actually happens is, python convert the above
calling of instance method to something like below:

SomeClass.inseart_to_arr(obj1, 6)
Now you know why you should always use self as the first parameter of instance methods in python and what really
happens behind the scene when we call a instance method. --Happy Coding!!
"""
