from db import getConnection
from models import products

def ensureTable():
    db = getConnection()
    cursor = db.cursor

    try :
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS products
        id INT PRIMARY KEY NUT NULL , 
        produt VARCHAR(255) NOT NULL ,
        price INT  NOT NULL,
        category VARCHAR(255) NOT NULL,
        """)

    except Exception as Eror:
        print(f"wrong in creating table : {Eror}")
    
    finally :
        db.commit()
        db.close()
