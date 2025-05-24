from model.habitat import Habitat
from dao.base_dao import BaseDAO

class HabitatDAO(BaseDAO):

    def insert(self, habitat: Habitat):
        with self.conn:
            cur = self.conn.execute(
                "INSERT INTO habitats (name) VALUES (?)",
                (habitat.name,)
            )
            habitat.id = cur.lastrowid

    def get_all(self):
        cur = self.conn.execute("SELECT id, name FROM habitats")
        return [Habitat(*row) for row in cur.fetchall()]