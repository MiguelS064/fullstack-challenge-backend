from app.database.connection import engine
from sqlalchemy import text

def top_aeropuerto():
    query = text("""
    SELECT a.nombre_aeropuerto, COUNT(*) as total
    FROM vuelos v
    JOIN aeropuertos a ON v.id_aeropuerto = a.id_aeropuerto
    GROUP BY a.nombre_aeropuerto
    HAVING COUNT(*) = (
        SELECT MAX(total) FROM (
            SELECT COUNT(*) as total
            FROM vuelos
            GROUP BY id_aeropuerto
        ) sub
    )
    """)

    with engine.connect() as conn:
        result = conn.execute(query)
        data = [dict(row._mapping) for row in result]

        return {
            "message": "Aeropuertos con mayor movimiento",
            "data": data
        }


def top_aerolinea():
    query = text("""
    SELECT al.nombre_aerolinea, COUNT(*) as total
    FROM vuelos v
    JOIN aerolineas al ON v.id_aerolinea = al.id_aerolinea
    GROUP BY al.nombre_aerolinea
    HAVING COUNT(*) = (
        SELECT MAX(total) FROM (
            SELECT COUNT(*) as total
            FROM vuelos
            GROUP BY id_aerolinea
        ) sub
    )
    """)

    with engine.connect() as conn:
        result = conn.execute(query)
        data = [dict(row._mapping) for row in result]

        return {
            "message": "Aerolíneas con mayor número de vuelos",
            "data": data
        }


def top_dia():
    query = text("""
    SELECT dia, COUNT(*) as total
    FROM vuelos
    GROUP BY dia
    HAVING COUNT(*) = (
        SELECT MAX(total) FROM (
            SELECT COUNT(*) as total
            FROM vuelos
            GROUP BY dia
        ) sub
    )
    """)

    with engine.connect() as conn:
        result = conn.execute(query)
        data = [dict(row._mapping) for row in result]

        return {
            "message": "Día(s) con mayor número de vuelos",
            "data": data
        }


def aerolineas_mas_2():
    query = text("""
    SELECT al.nombre_aerolinea, v.dia, COUNT(*) as total
    FROM vuelos v
    JOIN aerolineas al ON v.id_aerolinea = al.id_aerolinea
    GROUP BY al.nombre_aerolinea, v.dia
    HAVING COUNT(*) > 2
    """)

    with engine.connect() as conn:
        result = conn.execute(query)
        data = [dict(row._mapping) for row in result]

        if not data:
            return {
                "message": "Ninguna aerolínea tiene más de 2 vuelos por día",
                "data": []
            }

        return {
            "message": "Aerolíneas con más de 2 vuelos por día",
            "data": data
        }