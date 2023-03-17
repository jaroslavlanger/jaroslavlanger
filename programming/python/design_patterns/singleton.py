def is_singleton(factory):
    # todo: call factory() and return true or false
    # depending on whether the factory makes a
    # singleton or not
    called = 0

    def add_called(fu):
        nonlocal called
        called += 1
        return fu

    factory.__new__ = add_called(factory.__new__)
    factory.__init__ = add_called(factory.__init__)

    a = factory()
    b = factory()

    return True if a is b and called == 2 else False
