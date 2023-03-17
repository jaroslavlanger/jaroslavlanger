import pickle

class A:

    def __init__(self, *args):
        self.args = args

a = A(1,2,3)
b = A(1,2,3)

p_a = pickle.dumps(a)
p_b = pickle.dumps(b)

print(p_a == p_b)
