import os
import sqlite3
from pathlib import Path


class SqliteDB:
    def __init__(self, dict_cursor=False):
        self.dbname = os.path.join(Path(__file__).parent, "db_tables")
        self.dict_cursor = dict_cursor

    def __enter__(self, *args, **kwargs):
        self.conn = sqlite3.connect(self.dbname, timeout=180)
        self.cur = self.conn.cursor()
        return self

    def __exit__(self, *args, **kwargs):
        self.conn.commit()
        self.conn.close()

    def commit(self):
        self.conn.commit()

    def cur_lastrowvid(self):
        row = self.cur.lastrowid
        return row

    def fetchall(self, query, *args, **kwargs):
        self.cur.execute(query, *args, **kwargs)
        rows = self.cur.fetchall()
        if rows and self.dict_cursor:
            columns = [column[0] for column in self.cur.description]
            return [dict(zip(columns, row)) for row in rows]
        else:
            return rows

    def fetchone(self, query, *args, **kwargs):
        self.cur.execute(query, *args, **kwargs)
        row = self.cur.fetchone()
        if row and self.dict_cursor:
            column_names = [column[0] for column in self.cur.description]
            return dict(zip(column_names, row))
        return row

    def execute(self, query, *args, **kwargs):
        self.cur.execute(query, *args, **kwargs)