class Test(object):
    def __init__(self):
        self.a = 'a'
        self.b = 'b'

    def __setattr__(self, name, value):
        print 'set %s to %s' % (name, repr(value))

        if name in ('a', 'b'):
            object.__setattr__(self, name, value)


t = Test()
t.c = 'z'
setattr(t, 'd', '888')
