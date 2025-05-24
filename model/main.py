from model.animal import Animal
from model.habitat import Habitat
from dao.dao_factory import DAOFactory

dao_factory = DAOFactory()
animalDAO = dao_factory.get_animal_dao()
habitatDAO = dao_factory.get_habitat_dao()

savanne = Habitat(None, "Savanne")
desert = Habitat(None, "Wüste")
habitatDAO.insert(savanne)
habitatDAO.insert(desert)

leo = Animal(None, "Leo", "Löwe", 5, savanne.id)
zebra = Animal(None, "Zebulon", "Zebra", 8, savanne.id)
lezard = Animal(None, "Lizzi", "Lezzard", 5, desert.id)
animalDAO.insert(leo)
animalDAO.insert(zebra)
animalDAO.insert(lezard)

# Tiere in Habitat auslesen
print(f"Habitat: {savanne.name}")
for a in animalDAO.get_by_habitat(savanne.id):
    print(f" - {a.name} {a.species} ({a.age})")

# Tiere in Habitat auslesen
print(f"Habitat: {desert.name}")
for a in animalDAO.get_by_habitat(desert.id):
    print(f" - {a.name} {a.species} ({a.age})")