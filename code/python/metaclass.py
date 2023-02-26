

type_call = type.__call__

def print_dec(fu):

    def pd(*args, **kwargs):
        return fu(*args, **kwargs)

    return pd

# type.__call__ = print_dec(type.__call__)
# print = lambda *args: None

class Meta(type):

    def __call__(self, *args, **kwargs):
        print('Meta(type) was called')
        super(Meta, self).__call__(*args, **kwargs)

class A(metaclass=Meta):
    pass

A()
