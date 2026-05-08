from database.DB_connect import DBConnect
from model.airport import Airport
from model.rotta import Rotta


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllAirports():
        conn = DBConnect.get_connection()
        res = []
        cursor = conn.cursor(dictionary=True)
        query = """SELECT *
                    FROM airports"""
        cursor.execute(query)
        for row in cursor:
            res.append(Airport(**row))
        cursor.close()
        conn.close()
        return res

    @staticmethod
    def getAllRotte(distance):
        conn = DBConnect.get_connection()
        res = []
        cursor = conn.cursor(dictionary=True)
        query = """SELECT ORIGIN_AIRPORT_ID, DESTINATION_AIRPORT_ID, AVG(DISTANCE) as media
                    FROM flights
                    GROUP BY ORIGIN_AIRPORT_ID, DESTINATION_AIRPORT_ID
                    HAVING media > %s"""
        cursor.execute(query, (distance,))
        for row in cursor:
            res.append(Rotta(**row))
        cursor.close()
        conn.close()
        return res
