from random import randint

class Generator:
    def generate(self, count):
        return [randint(1,9) for x in range(count)]

class Splitter:
    def split(self, array):
        result = []

        row_count = len(array)
        col_count = len(array[0])

        for r in range(row_count):
            the_row = []
            for c in range(col_count):
                the_row.append(array[r][c])
            result.append(the_row)

        for c in range(col_count):
            the_col = []
            for r in range(row_count):
                the_col.append(array[r][c])
            result.append(the_col)

        diag1 = []
        diag2 = []

        for c in range(col_count):
            for r in range(row_count):
                if c == r:
                    diag1.append(array[r][c])
                r2 = row_count - r - 1
                if c == r2:
                    diag2.append(array[r][c])

        result.append(diag1)
        result.append(diag2)

        return result

class Verifier:
    def verify(self, arrays):
        first = sum(arrays[0])

        for i in range(1, len(arrays)):
            if sum(arrays[i]) != first:
                return False

        return True

class MagicSquareGenerator:

    MAXIMUM_ATTEMPTS = 1000

    def __init__(self):
        self.generator = Generator()
        self.splitter = Splitter()
        self.verifier = Verifier()

    def _generate(self, size):
        list_1d = self.generator.generate(size)
        side = int(size ** (1/2))
        return [list_1d[offset:offset+side] for offset in range(side)]


    def generate(self, size):
        magic_square = self._generate(size)
        for _ in range(self.MAXIMUM_ATTEMPTS):
            if self.verifier.verify(self.splitter.split(magic_square)):
                break
            magic_square = self._generate(size)
        else:
            raise Exception(('Bad luck for {attempts} attempts!'
                             'Square `{square}`'
                             ).format(attempts=self.MAXIMUM_ATTEMPTS,
                                      square=magic_square))
        print(f'DEBUG: Magic square was found after {_} attempts.')

        return magic_square

if __name__ == '__main__':
    magic_square = MagicSquareGenerator().generate(9)
    print(magic_square)
