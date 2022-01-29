from unittest.mock import Mock
from typing import Any

class ModelMock(Mock):

    def create_memento(self) -> object:
        return self.state

    def set_memento(self, memento: Any) -> None:
        self.state = memento

class Caretaker:

    def __init__(self, model):
        self._model = model

    def get_memento(self):
        return self._model.create_memento()

model_mock = ModelMock()

model_mock.state = 'ready'
print(f'{model_mock.state=}')
memento = model_mock.create_memento()
print(f'{memento=}')
model_mock.state = 'moving up'
print(f'{model_mock.state=}')
model_mock.set_memento(memento)
print(f'{model_mock.state=}')

c = Caretaker(model_mock)
print(f'{c.get_memento()=}')
