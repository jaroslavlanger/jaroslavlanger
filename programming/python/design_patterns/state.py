"""Switch-based State Machine
1) If the lock has just been locked (or at startup), the status is LOCKED.
2) If a digit has been entered, that digit is shown on the screen. As the user enters more digits, they are added to Status.
3) If the user has entered the correct sequence of digits, the lock status changes to OPEN.
4) If the user enters an incorrect sequence of digits, the lock status changes to ERROR.
"""
import unittest

class CombinationLock:
    def __init__(self, combination):
        self.status = 'LOCKED'
        self._combination = ''.join(str(i) for i in combination)

    def reset(self):
        self.status = 'LOCKED'

    def enter_digit(self, digit):
        d = str(digit)
        if self.status == 'LOCKED':
            self.status = d
        else:
            self.status += d

        if not self._combination.startswith(self.status):
            self.status = 'ERROR'
        elif self.status == self._combination:
            self.status = 'OPEN'


class FirstTestSuite(unittest.TestCase):
    def test_success(self):
        cl = CombinationLock([1, 2, 3, 4, 5])
        self.assertEqual('LOCKED', cl.status)
        cl.enter_digit(1)
        self.assertEqual('1', cl.status)
        cl.enter_digit(2)
        self.assertEqual('12', cl.status)
        cl.enter_digit(3)
        self.assertEqual('123', cl.status)
        cl.enter_digit(4)
        self.assertEqual('1234', cl.status)
        cl.enter_digit(5)
        self.assertEqual('OPEN', cl.status)

if __name__ == '__main__':
    unittest.main()
