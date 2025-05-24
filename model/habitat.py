from model.animal import Animal

class Habitat:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        #self.animals =[] Liste von Animal-Objekten

    def add_animal(selfself, animal):
        if isinstance(animal, Animal):
            self.animals.append(animal)

    def list_animals(self):
        print(f"In {self.name} leben:")
        for animal in self.animals:
            print(f"- {animal.name}, ein {animal.species}, {animal.age} Jahre alt")


