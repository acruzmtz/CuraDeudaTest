from models.database import Connection

db = Connection()


def search_by_name(name, table):
    fields = {"estado": "d_estado", "municipio": "d_mnpio", "colonia": "d_asenta"}

    sql = f"""
    SELECT * FROM {table} WHERE {fields[table]} LIKE '%{name}%'
    """
    try:
        data = db.execute(sql)
    except Exception as e:
        return False

    return data


def search_suburb_by_postal_code(postal_code):
    sql = f"""
    SELECT * FROM colonia WHERE d_codigo = {postal_code} LIMIT 1
    """
    try:
        data = db.execute(sql)
    except Exception as e:
        return False

    return data


def create_new_state(code, description):
    sql = f"""
    INSERT INTO estado (c_estado, d_estado)
    VALUES ('{code}', '{description}')
    """
    try:
        db.execute(sql)
    except Exception as e:
        return False

    return True


def create_new_township(code, description):
    sql = f"""
    INSERT INTO municipio (c_mnpio, d_mnpio)
    VALUES ('{code}', '{description}')
    """
    try:
        db.execute(sql)
    except Exception as e:
        return False

    return True


def create_new_suburb(code, description):
    sql = f"""
    INSERT INTO colonia (d_codigo, d_asenta)
    VALUES ('{code}', '{description}')
    """
    try:
        db.execute(sql)
    except Exception as e:
        return False

    return True
