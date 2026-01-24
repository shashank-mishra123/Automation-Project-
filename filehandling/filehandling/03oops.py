#create an abstract class employee with method  calculate salary().implement it for fullTimeemployee and parttime employee
from abc import ABC, abstractmethod
class employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class fullTimeEmployee(employee):
    def __init__(self,monthly_salary):
        self.monthly_salary=monthly_salary

    def calculate_salary(self):
        print("Full Time Employee Salary:",self.monthly_salary)

class parttimeemployee(employee):
    def __init__(self, partimesalary):
        self.patimesalary =partimesalary

    def calculate_salary(self):
        print("part time salary is ",self.patimesalary)


full =fullTimeEmployee(50000)
full.calculate_salary()
part = parttimeemployee(5000)
part.calculate_salary()
        