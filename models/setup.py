from models.database import Connection
from models.sql.tables import STATE, TOWNSHIP, SUBURB, ADD_COLUM_MUNICIPIO, ADD_FK_MUNICIPIO, ADD_COLUM_COLONIA, ADD_FK_COLONIA


def create_tables():
    db = Connection()

    try:
        db.execute(STATE)
        db.execute(TOWNSHIP)
        db.execute(SUBURB)
        db.execute(ADD_COLUM_MUNICIPIO)
        db.execute(ADD_FK_MUNICIPIO)
        db.execute(ADD_COLUM_COLONIA)
        db.execute(ADD_FK_COLONIA)
    except Exception as e:
        return False
    else:
        return True
