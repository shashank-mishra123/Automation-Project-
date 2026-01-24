#implementation the password validation using setter and setter

class login():
    def __init__(self):
        self.password="Sitaram"

    def get_password(self):
        return self.password
    
    def set_password(self):
        if self.password=="Sitaram":
            print(" is valid password  welcom to ")
        else:
            return " not valid "

user = login()
user.get_password()
user.set_password()
