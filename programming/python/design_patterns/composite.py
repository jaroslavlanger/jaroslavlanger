from abc import ABC
from collections.abc import Iterable
import unittest

class Summable(Iterable, ABC):

    @property
    def sum(self):
        summa = 0
        for v in self:
            summa += v.value
        return summa

class SingleValue(Summable):
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        yield self

class ManyValues(list, Summable):

    def append(self, something):
        if isinstance(something, Summable):
            for value in something:
                super().append(value)
        else:
            super().append(SingleValue(something))


class FirstTestSuite(unittest.TestCase):
    def test(self):
        single_value = SingleValue(11)
        other_values = ManyValues()
        other_values.append(22)
        other_values.append(33)
        # make a list of all values
        all_values = ManyValues()
        all_values.append(single_value)
        all_values.append(other_values)
        self.assertEqual(all_values.sum, 66)

if __name__ == '__main__':
    unittest.main()
