import unittest

class Sentence:

    class Modifier:
        def __init__(self, index, capitalize=False):
            self.index = index
            self.capitalize = capitalize

    def __init__(self, plain_text):
        self.words = plain_text.split(' ')
        self.modifiers = {}

    def __getitem__(self, key):
        if key not in self.modifiers:
            modifier = self.Modifier(key)
            self.modifiers[key] = modifier
        return self.modifiers[key]

    def get_modified_words(self):
        for i in range(len(self.words)):
            if i in self.modifiers and self.modifiers[i].capitalize:
                yield self.words[i].upper()
            else:
                yield self.words[i]

    def __str__(self):
        return ' '.join(word for word in self.get_modified_words())


class TestSentence(unittest.TestCase):

    def test_capitalize(self):
        sentence = Sentence('hello world')
        sentence[1].capitalize = True
        self.assertEqual('hello WORLD', str(sentence))

if __name__ == '__main__':
    unittest.main()
