class Originator:
    name = 'Originator'
    age = 10
    color = 'violet'

class Memento:

    def __init__(self, originator: Originator) -> None:
        self._state = (originator.name,
                       originator.age,
                       originator.color)

    def __iter__(self):
        return iter(self._state)

    def __iter__(self):
        yield self._state[0]
        yield self._state[1]
        yield self._state[2]


o = Originator()
m = Memento(o)
print(m)
name, age, color = m
print(name, age, color)
