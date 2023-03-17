import unittest

class Event(list):
    def __call__(self, *args, **kwargs):
        for observer in self:
            observer(*args, **kwargs)

    def subscribe(self, who):
        self.append(who)

    def unsubscribe(self, who):
        self.remove(who)

class Game:
    def __init__(self):
        self._rats = 0
        self.rats_increased = Event()
        self.rats_decreased = Event()

    @property
    def attack(self):
        return self._rats

    @attack.setter
    def attack(self, value):
        if value > self._rats:
            self.rats_increased()
        elif value < self._rats:
            self.rats_decreased()
        self._rats = value

class Rat:
    def __init__(self, game):
        self.game = game
        self.attack = game.attack
        self.game.rats_increased.append(self.increase_attack)
        self.game.rats_decreased.append(self.decrease_attack)
        self.game.attack = self.game.attack + 1

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback): 
        self.game.rats_increased.remove(self.increase_attack)
        self.game.rats_decreased.remove(self.decrease_attack)
        self.game.attack = self.game.attack - 1

    def increase_attack(self):
        self.attack += 1

    def decrease_attack(self):
        self.attack -= 1

class GameTest(unittest.TestCase):
    def test_three_rats_one_dies(self):
        game = Game()

        rat = Rat(game)
        self.assertEqual(1, rat.attack)

        rat2 = Rat(game)
        self.assertEqual(2, rat.attack)
        self.assertEqual(2, rat2.attack)

        with Rat(game) as rat3:
            self.assertEqual(3, rat.attack)
            self.assertEqual(3, rat2.attack)
            self.assertEqual(3, rat3.attack)

        self.assertEqual(2, rat.attack)
        self.assertEqual(2, rat2.attack)

if __name__ == '__main__':
    unittest.main()
