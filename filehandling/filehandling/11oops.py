#write a program where salary is cannot be set a below wage
class Employee_salary():
    def __init__(self):
        self.__salary=10000
    
    @property
    def set_salary(self):
        if self.__salary<100:
            return self.__salary
        else:
            return self.__salary+10000
employee = Employee_salary()
print(employee.set_salary)
    