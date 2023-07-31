class xyz():
    def __init__(self, name, **kwargs):
        self.name = name
        for key in kwargs:
            exec("self.%s = kwargs.get(key)" % (key))


a = xyz('Vivek', age=10, job='IT')
print(a.name)
print(a.age)
print(a.job)
