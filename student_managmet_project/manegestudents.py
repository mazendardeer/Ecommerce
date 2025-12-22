class student():
    def __init__(self,id,name,age):
        self.id = int(id)
        self.name = name
        self.age = int(age) 
    
    def __str__(self):
        return f"ID : {self.id} , name : {self.name} , age : {self.age} \n "

class studentManeger :
    def __init__(self):
        self.students = []

    def addStudent(self,student):
        for s in self.students :
            if s.id == student.id :
                print(f"id : {student.id} is already exist!")
                return
        self.students.append(student)
        print(f"id :{student.id} is added \n")

    def removeStudent(self,id):
        for s in self.students :
            if s.id == id :
                self.students.remove(s)
                print(f"id : {id} is removed.\n")
                return 
        print(f" id :{id} is not exist!")
       
    def showStudents(self):
        if self.students:
            print("the students in  the school :\n")
            for i in self.students :
                print(i)
        else:
            print("Sorry : No students in the school!")
        
        

