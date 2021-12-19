from models.database import Connection


def read_tables(path):
    with open(path, 'r') as file:
        return file.read()


def create_tables():
    db = Connection()
    path = "models/sql/tables.sql"
    sql = read_tables(path)

    try:
        db.execute(sql)
    except Exception as e:
        return False
    else:
        return True
