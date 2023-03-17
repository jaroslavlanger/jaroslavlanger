A = 'constant'

class Test:

    class_attrib = 10

    def __init__(self):
        self.name = self.__class__.__name__
        self.v = 'a'
        self.l = [1,2,3]
        self.d = {1: 'a',  2: 'b', 3: 'c'}
        breakpoint()

    def method(self):
        pass

t = Test()
