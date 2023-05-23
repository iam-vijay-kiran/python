###  OOPS through Python  ###
## Class --> objects (functions)
# class has attributes & behaviour 
# attribute = stores values for object   &&   behaviour = methods which shows the properties of a particular object

# How to create a class in python

class Employee:

    # Constructor of class
    def __init__(self, name, salary):
        self.emp_name = name
        self.emp_salary = salary 
    
    # method of class
    def displayEmployeeInfo(self):
        print("Employee name : ", self.emp_name, "Employee Salary : ", self.emp_salary) 
