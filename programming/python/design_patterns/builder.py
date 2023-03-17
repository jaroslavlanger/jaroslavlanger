"""class Person:
  def __init__(self):
    self.name = ""
    self.age = 0
"""

class Code:

    INDENTATION = '  '

    def __init__(self, line):
        self.line = line
        self.members = []

    def add_member(self, member):
        self.members.append(member)

    def pop_member(self):
        self.members.pop()

    def to_string(self, indent):
        code = ['{}{}\n'.format(self.INDENTATION*indent, self.line)]
        for member in self.members:
            code.append(member.to_string(indent+1))

        return ''.join(code)

    def __str__(self):
        return self.to_string(0)

class CodeBuilder:

    def __init__(self, root_name):
        self._root = Code('class {}:'.format(root_name))
        self._root.add_member(Code('pass'))
        self._init = None

    def add_field(self, type, name):
        if self._init is None:
            self._root.pop_member()
            self._init = Code('def __init__(self):')
            self._root.add_member(self._init)

        self._init.add_member(Code('self.{} = {}'.format(type, name)))
        return self

    def __str__(self):
        return str(self._root)


if __name__ == '__main__':
    cb = CodeBuilder('Person').add_field('name', '""') \
                              .add_field('age', '0')

    print(str(cb), end='')
    assert str(cb) == __doc__
