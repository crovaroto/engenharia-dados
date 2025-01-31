class Foo:
    def __init__(self, x = None) -> None:
        self._x = x

    @property
    def x(self):
        return self._x or 0

    @x.setter
    def x(self, value):
        self._x += value

    @x.deleter
    def x(self):
        self._x = -1 

foo = Foo(10)
print(foo.x)# 10 
foo.x =  10 # setter
print(foo.x)# 20
del foo.x
print(foo.x)