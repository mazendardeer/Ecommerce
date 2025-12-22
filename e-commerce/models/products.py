from db import getConnection

class Product():
    def __init__(self,id,name,price,category, stock=0):
        self.id = id 
        self.name= name
        self.price = float(price)
        self.category = category
        self.stock = int(stock)

    def __str__(self):
        return f"\n id : {self.id} \n product : {self.name} \n price : {self.price} \n category : {self.category} \n"

def productTable():
    db = getConnection()
    cursor = db.cursor()

    try :
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS products(
        id INT PRIMARY KEY AUTO_INCREMENT , 
        name VARCHAR(255) NOT NULL ,
        price DECIMAL(10,2)  NOT NULL,
        category VARCHAR(255) NOT NULL,
        stock INT NOT NULL)
        
        """)

    except Exception as Error:
        print(f"wrong in creating table : {Error}")
    
    finally :
        db.commit()
        db.close()

def productInsertion(product):
    db = getConnection()
    cursor = db.cursor()

    try :
        sql = "INSERT INTO products(name,price,category,stock) VALUES(%s,%s,%s,%s)"
        cursor.execute(sql,(product.name,product.price,product.category,product.stock))
        print("the product insertion is done..")
        product.id = cursor.lastrowid
        return product.id

    except Exception as Error :
        print("wrong in data insertion..")

    finally :
        db.commit()
        cursor.close()
        db.close()



