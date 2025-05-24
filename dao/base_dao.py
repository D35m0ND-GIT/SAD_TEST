class BaseDAO:
    def __init__(self, conn):
        self.conn = conn

    def query_all(self, sql, row_mapper, params=None):
        cur = self.conn.execute(sql, params or ())
        return [row_mapper(row) for row in cur.fetchall()]

    def query_one(self, sql, row_mapper, params=None):
        cur = self.conn.execute(sql, params or ())
        row = cur.fetchone()
        return row_mapper(row) if row else None