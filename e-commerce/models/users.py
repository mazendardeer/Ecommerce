from werkzeug.security import check_password_hash, generate_password_hash
from db import getConnection

class User():
    def __init__(self, name, email, password, id=None):
        self.id = id
        self.name = name
        self.email = email
        self.password_hash = generate_password_hash(password)

    def __str__(self):
        return f"\n Id = {self.id} \n name = {self.name} \n email = {self.email} \n"

    def checkPassword(self, password):
        return check_password_hash(self.password_hash, password)

# إنشاء جدول المستخدمين
def usersTable():
    db = getConnection()
    cursor = db.cursor()
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users(
                id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL UNIQUE,
                password_hash VARCHAR(255) NOT NULL
            )
        """)
        print("Users table created.")
    except Exception as Error:
        print(f"Error creating users table: {Error}")
    finally:
        db.commit()
        cursor.close()
        db.close()

# تسجيل مستخدم جديد
def register(user):
    db = getConnection()
    cursor = db.cursor(buffered=True)

    try:
        # التحقق إذا كان البريد موجود مسبقاً
        cursor.execute("SELECT id FROM users WHERE email=%s", (user.email,))
        result = cursor.fetchone()

        if result is None:
            cursor.execute(
                "INSERT INTO users(name, email, password_hash) VALUES (%s, %s, %s)",
                (user.name, user.email, user.password_hash)
            )
            user_id = cursor.lastrowid
            print("Data inserted correctly in the table.")
            return user_id
        else:
            print("User already exists in the system.")
            return result[0]

    except Exception as Error:
        print(f"Error in data insertion: {Error}")

    finally:
        db.commit()
        cursor.close()
        db.close()
