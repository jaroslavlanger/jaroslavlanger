from __future__ import annotations
from abc import ABC, abstractmethod
from collections.abc import Iterable, Iterator, Sequence
from typing import runtime_checkable, Protocol, overload, TypeVar, Union

import numpy as np

T = TypeVar('T')

# @runtime_checkable
class Vector(Protocol[T]):
    """Generic Vector protocol"""

    @abstractmethod
    def __iter__(self) -> Iterator[T]:
        """Retrurn iterator of its elements."""

    @abstractmethod
    def __len__(self) -> int:
        """Returns number of elements."""

    @overload
    @abstractmethod
    def __getitem__(self, key: int) -> T:
        ...

    @overload
    @abstractmethod
    def __getitem__(self, key: slice) -> Vector[T]:
        ...

    @abstractmethod
    def __getitem__(self, key: Union[int, slice]) -> Union[T, Vector[T]]:
        """Returns its element or vector of elements."""

    @overload
    @abstractmethod
    def __setitem__(self, key: int, value: T) -> None:
        ...

    @overload
    @abstractmethod
    def __setitem__(self, key: slice, value: Iterable[T]) -> None:
        ...

    @abstractmethod
    def __setitem__(self, key: Union[int, slice],
                    value: Union[T, Iterable[T]]) -> None:
        """Sets its element or elements."""

    @abstractmethod
    def __neg__(self) -> Vector:
        """Returns vector of its negated elements."""

    @abstractmethod
    def __add__(self, vector: Iterable[T]) -> Vector[T]:
        """Returns vector created from addition of given vector to self.

        Length of returned vector is max(len(self), len(vector)).
        """

    @abstractmethod
    def __mul__(self, multiplier: T) -> Vector[T]:
        """Returns vector of its multiplied elements by multiplied."""

    @abstractmethod
    def __truediv__(self, divisor: T) -> Vector[T]:
        """Returns vector of its divided elements by divisor."""

    @abstractmethod
    def norm(self, p: int = 2) -> T:
        """Returns its Lp-norm."""

class VectorReal(Vector[float]):

    def __init__(self, elements: Sequence[float]):
        self._elements = list(elements)

    def __add__(self, vector: Vector[float]) -> VectorReal:
        return self.__class__(self._elements)

def check_is_vector(vector: Vector) -> bool:
    return isinstance(vector, Vector)

array: Vector = np.array([])

print(check_is_vector(array))

vector = VectorReal([])

print(check_is_vector(np.array([])))
