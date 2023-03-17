"""For more information see: https://docs.python.org/3/library/enum.html"""
from enum import Enum
from enum import auto

class EnumAutoLower(Enum):
    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return name.lower()

class Keys(EnumAutoLower):
    """Keyboard key enumeration."""
    ESCAPE = auto()
    LEFT = auto()
    RIGHT = auto()
    UP = auto()
    DOWN = auto()
    SPACE = auto()
    A = auto()
    D = auto()
    E = auto()
    Q = auto()
    S = auto()
    W = auto()
    X = auto()

print('for e in Keys:')
for e in Keys:
    print(f'    {e=}')
