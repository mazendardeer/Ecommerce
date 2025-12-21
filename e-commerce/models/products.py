from db import getConnection

class Product():
    def __init__(self,id,name,price,category,image , stock=0):
        self.id = id 
        self.name= name
        self.price = float(price)
        self.category = category
        self.stock = int(stock)
        self.image = image

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
            stock INT NOT NULL,
            image VARCHAR(255))
            """)

        except Exception as Error:
            print(f"wrong in creating table : {Error}")
        
        finally :
            db.commit()
            db.close()
    
    def productInsertion(product):
        db = getConnection()
        cursor = db.cursor()
        Product.productTable()
    
        try :
            sql = "INSERT INTO products(name,price,category,image,stock) VALUES(%s,%s,%s,%s,%s)"
            cursor.execute(sql,(product.name,product.price,product.category,product.image,product.stock))
            print("the product insertion is done..")
            product.id = cursor.lastrowid
            return product.id
    
        except Exception as Error :
            print(f"wrong in data insertion..{Error}")
    
        finally :
            db.commit()
            cursor.close()
            db.close()

    def get_product():
        db = getConnection()
        cursor = db.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM products")
            data = cursor.fetchall()
            products = []
            for row in data :
                products.append(Product(row["id"],row["name"],row["price"],row["category"],row["image"],row["stock"]))

            return products

        except Exception as Error :
            print(f"wrong in show data : {Error}")    

        finally : 
            cursor.close()
            db.close()




