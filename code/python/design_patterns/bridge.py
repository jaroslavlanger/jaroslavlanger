"""
class Shape:
    def __init__(self):
        self.name = None


class Triangle(Shape):
    def __init__(self):
        super().__init__()
        self.name = 'Triangle'


class Square(Shape):
    def __init__(self):
        super().__init__()
        self.name = 'Square'


class VectorSquare(Square):
    def __str__(self):
        return f'Drawing {self.name} as lines'


class RasterSquare(Square):
    def __str__(self):
        return f'Drawing {self.name} as pixels'

# imagine VectorTriangle and RasterTriangle are here too
"""
from abc import ABC

class Renderer(ABC):
    @property
    def what_to_render_as(self):
        return None

# TODO: reimplement Shape, Square, Triangle and Renderer/VectorRenderer/RasterRenderer

class VectorRenderer(Renderer):

    @property
    def what_to_render_as(self):
        return 'lines'

class RasterRenderer(Renderer):

    @property
    def what_to_render_as(self):
        return 'pixels'


class Shape:

    def __init__(self, renderer):
        self.renderer = renderer
        self.name = self.__class__.__name__

    def __str__(self):
        return 'Drawing {name} as {what}'.format(name=self.name, what=self.renderer.what_to_render_as)

class Square(Shape):
    pass

class Triangle(Shape):
    pass
