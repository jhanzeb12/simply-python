# Singleton

class Singleton(object):
    __instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(Singleton, cls).__new__(cls, *args, **kwargs)

        return cls.__instances[cls]


class MyClass(Singleton):
    __fname = None

    def set_fname(self, fname):
        self.__fname = fname

    def get_fname(self):
        return self.__fname


c1 = MyClass()
c1.set_fname('Zaib')
print(c1.get_fname())
c2 = MyClass()
# shoudl return the name set with the instance c1
print(c2.get_fname())