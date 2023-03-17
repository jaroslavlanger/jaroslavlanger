from functools import wraps

class Class:

    @staticmethod
    def autosave(callable_):
        @wraps(callable_)
        def wrapper(self, *args, **kwargs):
            result = callable_(self, *args, **kwargs)
            self.save()
            return result
        return wrapper

    def save(self):
        print('"save" is being called.')

    @autosave
    def method(self):
        print('"method" is being called.')
        return 'result'

c = Class()
print(c.method())
