import mysql.connector

def getConnection():
    return  mysql.connector.connect(
        host     = "localhost",
        user     = "root",
        password = "123456",
        database = "ecommerce"
    )

