from manegestudents import student, studentManeger
from storage import saveStudent, removeStudent, loadStudent

def main():
    manager = studentManeger()
    
    while True:
        print("\n1- Add student to the school."
              "\n2- Remove student from the school."
              "\n3- Show the students in the school."
              "\n4- Quit from the menu.\n")
        
        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("❌ Please enter a valid number.")
            continue
        
        if choice == 1:
            try:
                id = int(input("Enter the student ID: "))
                name = input("Enter the student name: ")
                age = int(input("Enter the student age: "))
                s = student(id, name, age)
                manager.addStudent(s)
                saveStudent(s)
            except ValueError:
                print("❌ ID and age must be numbers.")
        
        elif choice == 2:
            try:
                id = int(input("Enter the student ID to remove: "))
                manager.removeStudent(id)
                removeStudent(id)
            except ValueError:
                print("❌ ID must be a number.")
        
        elif choice == 3:
            students = loadStudent()
            if students:
                for s in students:
                    print(s)
            else:
                print("No students in the school!")
        
        elif choice == 4:
            print("✅ Exiting the menu...")
            break
        
        else:
            print("❌ Please enter a valid choice (1-4).")

if __name__ == "__main__" :
    main()

