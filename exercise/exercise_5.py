def myfunc():
    """
        This is my func
    :return:
    """
    pass


print myfunc.__doc__


class myclass(object):
    """
        My Class
    """

    def __init__(self):
        pass

    def myfunc(self):
        """
            This is my func in class
        :return:
        """


print myclass.__doc__
obj = myclass()
print obj.myfunc.__doc__
