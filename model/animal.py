class Animal:
    def __init__(self, id, name, species, age, habitat_id=None):
        self.id = id
        self.name = name
        self.species = species
        self.age = age
        self.habitat_id = habitat_id

    def speak(self):
        print(f"{self.name} the {self.species} makes a sound.")