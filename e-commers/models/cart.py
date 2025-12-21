from db import getConnection

class Cart():
    def __init__(self, user_id) :
        self.user_id = user_id
    
    def createTable(self):
        try:
            db = getConnection()
            cursor = db.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS cart (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL UNIQUE,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE)ENGINE=InnoDB            
                """)            

        except Exception as Error :
            print (f"wrong in creat cart table..{Error}")

        finally:
            db.commit()
            cursor.close()
            db.close()

    def createCard_item(self):
        try:
            db = getConnection()
            cursor = db.cursor() 
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS cart_item(
                id INT AUTO_INCREMENT PRIMARY KEY,
                cart_id INT NOT NULL,
                product_id INT NOT NULL,
                quantity INT NOT NULL,
                FOREIGN KEY(cart_id) REFERENCES cart(id),
                FOREIGN KEY(product_id) REFERENCES products(id) ON DELETE CASCADE
            )ENGINE=InnoDB
            """)
        except Exception as Error :
            print(f"wrong in creat cart item table..{Error}") 

        finally:
            db.commit()
            cursor.close()
            db.close()


    def cartAdd(self,product_id,quantity=1):
        try:
            db = getConnection()
            cursor = db.cursor()
            cursor.execute("SELECT id FROM cart WHERE user_id=%s",(self.user_id,))
            cart = cursor.fetchone()
            if cart == None :
                cursor.execute("INSERT INTO cart (user_id) VALUES(%s)",(self.user_id,))
                cart_id = cursor.lastrowid
            else :
                cart_id = cart[0]

            cursor.execute("SELECT id , quantity FROM cart_item WHERE cart_id=%s AND product_id=%s",(cart_id,product_id))
            cart_item = cursor.fetchone()
            if cart_item == None :
                cursor.execute( "INSERT INTO cart_item (cart_id, product_id, quantity) VALUES (%s, %s, %s)",(cart_id, product_id, quantity))

            else :
                new_quantity = cart_item[1] + quantity
                cursor.execute("UPDATE cart_item SET quantity=%s WHERE id=%s",(new_quantity,cart_item[0]))

        except Exception as Error :
            print(f"wrong in the cart inserion..{Error}") 

        finally :
            db.commit()
            cursor.close()
            db.close()

    def cartRemove(self,card_id,product_id):
        db = getConnection()
        cursor = db.cursor()
        try:
            cursor.execute("SELECT id  , quantity  FROM card_item WHERE cart_id=%s AND product_id=%s",(card_id,product_id))
            item = cursor.fetchone()
            if item == None :
                print("the product not in the cart")

           # else:
                #cursor.execute("DELET ")
        except:
            pass