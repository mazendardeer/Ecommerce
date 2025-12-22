from db import get_connection
from manegestudents import student

def ensure_table():
    db = get_connection()
    cursor = db.cursor()
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS student (
                id INT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                age INT NOT NULL
            )
        """)
        db.commit()
    except Exception as e:
        print(f"Error creating table: {e}")
    finally:
        cursor.close()
        db.close()

def saveStudent(student):
    ensure_table()
    db = get_connection()
    cursor = db.cursor()
    try:
        sql = "INSERT INTO student(id, name, age) VALUES (%s, %s, %s)"
        data = (student.id, student.name, student.age)
        cursor.execute(sql, data)
        db.commit()
        print("✅ Done..")
    except Exception as err:
        print(f"Error saving student: {err}")
    finally:
        cursor.close()
        db.close()

def removeStudent(student_id):
    ensure_table()
    db = get_connection()
    cursor = db.cursor()
    try:
        sql = "DELETE FROM student WHERE id = %s"
        cursor.execute(sql, (student_id,))
        db.commit()
        if cursor.rowcount > 0:
            print("✅ The student is removed from database.")
        else:
            print("❌ Student not found.")
    except Exception as err:
        print(f"Error deleting student: {err}")
    finally:
        cursor.close()
        db.close()

def loadStudent():
    ensure_table()
    db = get_connection()
    cursor = db.cursor()
    students = []
    try:
        cursor.execute("SELECT id, name, age FROM student")
        result = cursor.fetchall()
        for row in result:
            s = student(row[0], row[1], row[2])
            students.append(s)
    except Exception as err:
        print(f"Error loading students: {err}")
    finally:
        cursor.close()
        db.close()
    return students
