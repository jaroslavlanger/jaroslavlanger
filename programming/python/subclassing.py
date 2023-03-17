class ClassA:

    def method(self):
        print('--- ClassA().method()')
        print(type(self).__name__)
        print(self.__class__.__mro__)
        print('--- ClassA().method()')

class ClassB():

    def method(self):
        print('--- ClassB().method()')
        print(self.__class__.__name__)
        print('--- ClassB().method()')

class ClassAB(ClassA, ClassB):

    def method(self):
        print('--- ClassAB().method()')
        print(self.__class__.__mro__)
        super(ClassAB, self).method()
        print('--- ClassAB().method()')

ClassAB().method()
