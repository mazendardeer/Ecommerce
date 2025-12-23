from werkzeug.security import check_password_hash , generate_password_hash

class User():
    def __init__(self,id,name,email,password) :
        self.id = id 
        self.name = name
        self.email = email
        self.password_hash = generate_password_hash(password)

    def __str__(self) :
        return f"\n Id = {self.id} \n name = {self.name} \n email = {self.email} \n"

    def checkPassword(self,password) :
        return check_password_hash(self.password_hash , password)
