# old style and new style class


class a():
    def test1(self):
        print("test1")


class A(a):
    def test2(self):
        print("test2")


class test(A):
    def test3(self):
        self.test1()


obj = test()
obj.test3()
