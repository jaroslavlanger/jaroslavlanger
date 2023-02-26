import unittest
from unittest import TestCase

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def resize(self, factor):
        self.radius *= factor

    def __str__(self):
        return 'A circle of radius {radius}'.format(radius=self.radius)

class Square:
    def __init__(self, side):
        self.side = side

    def __str__(self):
        return 'A square with side {side}'.format(side=self.side)


class ColoredShape:
    def __init__(self, shape, color):
        self.color = color
        self.shape = shape

    def resize(self, factor):
        try:
            self.shape.resize(factor)
        except:
            pass

    def __str__(self):
        return '{shape} has the color {color}'.format(shape=self.shape,
                                                      color=self.color)

#    def __getattr__(self, name):
#        return getattr(self.shape, name)
#
#    def __setattr__(self, name, value):
#        setattr(self.shape, name, value)
#
#    def __delattr__(self, name):
#        delattr(self.shape, name)


class Evaluate(TestCase):
    def test_circle(self):
        circle = ColoredShape(Circle(5), 'red')
        self.assertEqual(
          'A circle of radius 5 has the color red',
          str(circle)
        )
        circle.resize(2)
        self.assertEqual(
          'A circle of radius 10 has the color red',
          str(circle)
        )

if __name__ == '__main__':
    unittest.main()
