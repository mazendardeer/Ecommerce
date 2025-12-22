from werkzeug.security import check_password_hash , generate_password_hash
from db import getConnection

class User():
    def __init__(self,name,email,password,id=None) :
        self.id = id 
        self.name = name
        self.email = email
        self.password_hash = generate_password_hash(password)

    def __str__(self) :
        return f"\n Id = {self.id} \n name = {self.name} \n email = {self.email} \n"

    def checkPassword(self,password) :
        return check_password_hash(self.password_hash , password)

def usersTable():
    db = getConnection()
    cursor = db.cursor()

    try :
        cursor.execute("""CREATE TABLE IF NOT EXISTS users(
            id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
            name VARCHAR(255) NOT NULL ,
            email VARCHAR(255) NOT NULL UNIQUE ,
            password_hash VARCHAR(255) NOT NULL
        )
        """)
        print("the table is creat.") 

    except Exception as Error :
        print(f"wrong in creat users table : {Error}") 

    finally :
        db.commit()
        cursor.close()
        db.close()

def register(user):
    db = getConnection()
    cursor = db.cursor()

    try:
        cursor.execute("SELECT id FROM users WHERE email=%s"(user.email))
        result = cursor.fetchone()
        if result != None :
            sql = "INSERT INTO users( name , email, password_hash) VALUES( %s , %s , %s ) "
            cursor.execute(sql,(user.name,user.email,user.password_hash))
            print("the data insert in the table correctly..") 

        else:
            print('the user is already in the system...')

    except Exception as Error :
        print(f"wrong in data insertion : {Error}")

    finally:
        db.commit()
        cursor.close()
        db.close()
