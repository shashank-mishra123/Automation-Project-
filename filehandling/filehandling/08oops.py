# create a class user with properties __password and __email
class user():
    def __init__(self):
        self.__password="Sitaram"
        self.__email="kanhs2002@gmail.com"
    @property
    def get_password(self):
        return self.__password
    @property
    def get_email(self):
        return self.__email


Admin = user()
print(Admin.get_email)
print(Admin.get_password)