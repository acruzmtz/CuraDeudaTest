from models.database import Connection
from models.sql.tables import STATE, TOWNSHIP, SUBURB, SHIPPING, SET_FOREING_KEYS, SET_INDEX

# def read_tables(path):
#     with open(path, 'r') as file:
#         return file.read()


def create_tables():
    db = Connection()
    path = "models/sql/tables.sql"
    # sql = read_tables(path)

    try:
        db.execute(STATE)
        db.execute(TOWNSHIP)
        db.execute(SUBURB)
        db.execute(SHIPPING)
        db.execute(SET_INDEX)
        db.execute(SET_FOREING_KEYS)
    except Exception as e:
        return False
    else:
        return True
