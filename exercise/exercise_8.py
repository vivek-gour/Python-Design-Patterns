class abc():

    def __init__(self, *args, **kwargs):
        for arg in args:
            exec ('self.%s = "%s"' % (arg, arg))
        for kwarg in kwargs:
            exec('self.%s = "%s"' % (kwarg, kwargs[kwarg]))

    def printargs(self):
        print self.a, self.b, self.c
        print self.d, self.e, self.f


obj = abc('a', 'b', 'c', d=3, e=4, f=5)
obj.printargs()
