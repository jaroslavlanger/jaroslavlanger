"""See: docs.python.org/3/library/functools.html#functools.singledispatch"""
from functools import singledispatch
from enum import Enum, auto

class Privileges(Enum):
    NORMAL = auto()
    RESTRICTED = auto()
    SUPER = auto()

# restricted = ['a']
# normal = ['a', 'b']
# super_ = ['a', 'b', 'c']
# 
# 
# @singledispatch
# def make_aciton(privileges=Privileges.NORMAL, action=''):
#     if action in normal:
#         print(action)
# 
# @make_aciton.register
# def _(privileges=Privileges.RESTRICTED, action=''):
#     if verbose:
#         print("Strength in numbers, eh?", end=" ")
#     print(arg)
# 
# @make_aciton.register
# def _(arg: list, verbose=False):
#     if verbose:
#         print("Enumerate this:")
#     for i, elem in enumerate(arg):
#         print(i, elem)
# 
# make_aciton('Action A', verbose=True)
