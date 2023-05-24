###  OOPS through Python  ###
## Class --> objects (functions)
# class has attributes & behaviour 
# attribute = stores values for object   &&   behaviour = methods which shows the properties of a particular object

# How to create a class in python

class Employee:

    # Class attribute == inside the class but oustside object created
    empCount = 0

    # Constructor of class
    # it is mainly used for assignment of instance variables
    def __init__(self, name, salary):
        # instance variable or instance attributes  = inside class & object
        self.emp_name = name
        self.emp_salary = salary 
        Employee.empCount +=1               # using class attribute after instance attribute

    # method of class
    def displayEmployeeInfo(self):
        print("Employee name : ", self.emp_name, "Employee Salary : ", self.emp_salary) 

    def dispalyEmployeeCount(self):
        print("Employee Count : ", Employee.empCount)

emp1 = Employee("vijay", 4500)
emp1.displayEmployeeInfo()
emp1.dispalyEmployeeCount()

emp2 = Employee("ganesh", 4700)
emp2.displayEmployeeInfo()
emp2.dispalyEmployeeCount()

# we try to display again without passing data, which shows the count previously stored
emp1.dispalyEmployeeCount()
emp2.dispalyEmployeeCount()
