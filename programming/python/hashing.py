class Memento:

    def __init__(self):
        self.a = 1
        self.b = 2

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return bool(self.__dict__ == other.__dict__)
        return NotImplemented

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.values())))

m1 = Memento()
m2 = Memento()
m1.__hash__()
print(m1 == m2)
