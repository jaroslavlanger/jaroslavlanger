import unittest

class Person:
    def __init__(self, age):
        self.age = age

    def drink(self):
        return 'drinking'

    def drive(self):
        return 'driving'

    def drink_and_drive(self):
        return 'driving while drunk'

class ResponsiblePerson:
    def __init__(self, person):
        self.person = person

    @property
    def age(self):
        return self.person.age

    @age.setter
    def age(self, value):
        self.person.age = value

    def drink(self):
        if self.person.age < 18:
            return 'too young'
        else:
            return self.person.drink()

    def drive(self):
        if self.person.age < 16:
            return 'too young'
        else:
            return self.person.drive()

    def drink_and_drive(self):
        return 'dead'

class TestResponsiblePerson(unittest.TestCase):

    person = Person(18)
    person_young = Person(15)

    def test_drink(self):
        self.assertEqual('drinking', ResponsiblePerson(self.person).drink())
        self.assertEqual('too young', ResponsiblePerson(self.person_young).drink())

    def test_drive(self):
        self.assertEqual('driving', ResponsiblePerson(self.person).drive())
        self.assertEqual('too young', ResponsiblePerson(self.person_young).drive())

    def test_drink_and_drive(self):
        self.assertEqual('dead', ResponsiblePerson(self.person).drink_and_drive())
        self.assertEqual('dead', ResponsiblePerson(self.person_young).drink_and_drive())

if __name__ == '__main__':
    unittest.main()
