class Token:
    def __init__(self, value=0):
        self.value = value

class Memento(list):
    pass

class TokenMachine:
    def __init__(self):
        self.tokens = []

    def add_token_value(self, value):
        return self.add_token(Token(value))

    def add_token(self, token):
        self.tokens.append(token)
        return Memento(t.value for t in self.tokens)

    def revert(self, memento):
        self.tokens = list(Token(v) for v in memento)

if __name__ == '__main__':
    tm = TokenMachine()
    t = Token(111)
    tm.add_token(t)
    m1 = tm.add_token_value(222)
    t.value = 333

    tm.revert(m1)
    assert tm.tokens[0].value == 111
