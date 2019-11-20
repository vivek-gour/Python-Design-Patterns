
"""
global variable if defined in class or out side class and if we assign any value to it in inner method so that will be
treated as local variable in that method only

"""


class abc():
    global a

    def printa(self):
        print a, self.a

    a = 2


obj = abc()
obj.a = 1
print a
obj.printa()
