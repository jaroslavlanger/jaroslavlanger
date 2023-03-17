from copy import deepcopy

class TupleDeepcopy(tuple):

    def __new__(cls, *iterable):
        """Do not use @classmethod with __new__."""
        print(f'{cls=}, {iterable=}')
        return super().__new__(cls, (deepcopy(e) for e in iterable))

    def __iter__(self):
        yield from super().__iter__()

t = tuple([1,2,3,4])
print(f'{t=}')
td = TupleDeepcopy(1,2,3,4)
print(f'{td=}')

print(f'{(t == td)=}')
for t in td:
    print(t)
