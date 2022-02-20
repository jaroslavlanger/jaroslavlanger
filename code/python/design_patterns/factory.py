 class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class PersonFactory:

    def __init__(self):
        self.next_id = 0

    def create_person(self, name):
        person = Person(self.next_id, name)
        self.next_id += 1
        return person
