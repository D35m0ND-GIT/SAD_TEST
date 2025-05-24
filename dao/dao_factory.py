# Objekte mit einer Schnittstelle kreieren, um Komplexität zu reduzieren

from db.db import Database
from dao.animal_dao import AnimalDAO
from dao.habitat_dao import HabitatDAO

class DAOFactory:
    def __init__(self):
        self.db = Database()
        self.db.init_db()
        self.conn = self.db.get_connection()

    def get_animal_dao(self):
        return AnimalDAO(self.conn)

    def get_habitat_dao(self):
        return HabitatDAO(self.conn)