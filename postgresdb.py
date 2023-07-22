import os
import psycopg2
import psycopg2.extras
from decimal import Decimal

class PostgresDB:
    def __init__(self, dict_cursor=False):
        self.dbname = 'default_db'
        self.user = os.environ.get('DB_USER')
        self.password = os.environ.get('DB_PASSWORD')
        self.host = os.environ.get('DB_HOST')
        self.dict_cursor = dict_cursor

    def __enter__(self, *args, **kwargs):
        self.conn = psycopg2.connect(
            dbname=self.dbname, user=self.user,
            password=self.password, host=self.host
        )
        self.cur = self.conn.cursor(
            cursor_factory=psycopg2.extras.RealDictCursor if self.dict_cursor else None
        )
        return self

    def __exit__(self, *args, **kwargs):
        self.conn.commit()
        self.cur.close()
        self.conn.close()

    def commit(self):
        self.conn.commit()

    def fetchall(self, query, *args, **kwargs):
        self.cur.execute(query, *args, **kwargs)
        return self.cur.fetchall()

    def fetchone(self, query=None, *args, **kwargs):
        self.cur.execute(query, *args, **kwargs)
        return self.cur.fetchone()

    def execute(self, query, *args, **kwargs):
        self.cur.execute(query, *args, **kwargs)