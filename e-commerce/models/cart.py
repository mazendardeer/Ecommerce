from db import getConnection

class Cart:
    def __init__(self, guest_id):
        self.guest_id = guest_id

    @staticmethod
    def createTable():
        db = getConnection()
        cursor = db.cursor(buffered=True)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cart (
                id INT AUTO_INCREMENT PRIMARY KEY,
                guest_id VARCHAR(50) NOT NULL UNIQUE
            )
        """)
        db.commit()
        cursor.close()
        db.close()

    @staticmethod
    def createCart_Item():
        db = getConnection()
        cursor = db.cursor(buffered=True)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cart_item (
                id INT AUTO_INCREMENT PRIMARY KEY,
                cart_id INT NOT NULL,
                product_id INT NOT NULL,
                quantity INT NOT NULL,
                FOREIGN KEY (cart_id) REFERENCES cart(id) ON DELETE CASCADE,
                FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
            )
        """)
        db.commit()
        cursor.close()
        db.close()

    def cartAdd(self, product_id, quantity=1):
        db = getConnection()
        cursor = db.cursor(buffered=True)

        Cart.createTable()
        Cart.createCart_Item()

        try:
            cursor.execute("SELECT id FROM products WHERE id=%s", (product_id,))
            if cursor.fetchone() is None:
                return

            cursor.execute("SELECT id FROM cart WHERE guest_id=%s", (self.guest_id,))
            cart = cursor.fetchone()
            if cart is None:
                cursor.execute("INSERT INTO cart (guest_id) VALUES (%s)", (self.guest_id,))
                cart_id = cursor.lastrowid
            else:
                cart_id = cart[0]

            cursor.execute("""
                SELECT id, quantity FROM cart_item
                WHERE cart_id=%s AND product_id=%s
            """, (cart_id, product_id))

            item = cursor.fetchone()

            if item is None:
                cursor.execute("""
                    INSERT INTO cart_item (cart_id, product_id, quantity)
                    VALUES (%s, %s, %s)
                """, (cart_id, product_id, quantity))
            else:
                cursor.execute("""
                    UPDATE cart_item
                    SET quantity = quantity + %s
                    WHERE id=%s
                """, (quantity, item[0]))

        finally:
            db.commit()
            cursor.close()
            db.close()

    @staticmethod
    def view_cart(guest_id):
        db = getConnection()
        cursor = db.cursor(buffered=True, dictionary=True)

        try:

            cursor.execute("""
                SELECT 
                    p.id, p.name, p.price, ci.quantity
                FROM cart c
                JOIN cart_item ci ON c.id = ci.cart_id
                JOIN products p ON p.id = ci.product_id
                WHERE c.guest_id=%s
            """, (guest_id,))

            result = cursor.fetchall()

        except Exception as Error :
            print(f"wrong in data view : {Error}")

        finally:
            cursor.close()
            db.close()
            return result
    @staticmethod
    def delet_cart(product_id,guest_id):
        db = getConnection()
        cursor = db.cursor(buffered=True)

        try :
            cursor.execute("SELECT id FROM cart WHERE guest_id=%s",(guest_id,))
            cart = cursor.fetchone()
            cart_id = cart[0]

            cursor.execute("SELECT quantity FROM cart_item WHERE cart_id=%s AND product_id=%s",(cart_id,product_id))
            item = cursor.fetchone()
            quantity = item[0]
            if quantity > 1 :
                cursor.execute("UPDATE cart_item SET quantity = quantity - 1 WHERE cart_id=%s AND product_id=%s",(cart_id,product_id))

            else :
                cursor.execute("DELETE FROM cart_item  WHERE cart_id=%s AND product_id=%s",(cart_id,product_id))
            db.commit()

        except Exception as Error :
            print(f"wrong in delet product : {Error}")

        finally : 
            cursor.close()
            db.close()


