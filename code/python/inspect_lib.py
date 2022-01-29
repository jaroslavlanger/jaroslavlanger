import inspect

class c:
    def m(self):
        breakpoint()
        inspect.stack()

c().m()
