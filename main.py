from typing import Union


from excs_handle import handle_db_exceptions
from postgresdb import PostgresDB
from sqlitedb import SqliteDB


@handle_db_exceptions
def get_users(user_id: Union[int, tuple]) -> Union[list, None]:
    query = "SELECT * FROM users"
    params = tuple()
    if user_id:
        query += " WHERE user_id IN %s"
        params += (user_id, ) if isinstance(user_id, tuple) else ((user_id, ), )
    with PostgresDB(dict_cursor=True) as db:
        users = db.execute(query, params)
    return users