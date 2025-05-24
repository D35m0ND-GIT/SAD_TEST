from model.animal import Animal
from dao.base_dao import BaseDAO

class AnimalDAO(BaseDAO):
    def insert(self, animal: Animal):
        with self.conn:
            cur = self.conn.execute(
                "INSERT INTO animals (name, species, age, habitat_id) VALUES (?, ?, ?, ?)",
                (animal.name, animal.species, animal.age, animal.habitat_id)
            )
            animal.id = cur.lastrowid

    def get_all(self):
        cur = self.conn.execute("SELECT id, name, species, age, habitat_id FROM animals")
        return [Animal(*row) for row in cur.fetchall()]

    def get_by_habitat(self, habitat_id):
        return self.query_all(
            "SELECT id, name, species, age, habitat_id FROM animals WHERE habitat_id = ?",
            lambda row: Animal(*row), (habitat_id,)
    )