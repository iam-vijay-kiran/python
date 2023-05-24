###  OOPS through Python  ###
## Class --> objects (functions)
# class has attributes & behaviour 
# attribute = stores values for object   &&   behaviour = methods which shows the properties of a particular object

# How to create a class in python

class Employee:
    # Constructor of class
    # it is mainly used for assignment of instance variables
    def __init__(self, name, salary):
        # instance variable or instance attributes 
        self.emp_name = name
        self.emp_salary = salary 

    # method of class
    def displayEmployeeInfo(self):
        print("Employee name : ", self.emp_name, "Employee Salary : ", self.emp_salary) 

emp1 = Employee("vijay", 4500)
emp2 = Employee("ganesh", 4700)
emp1.displayEmployeeInfo()
emp2.displayEmployeeInfo()
        
print(emp1.emp_name)          # let emp1 @ 200 memory location, then emp1.emp_name calls name @ emp1 location
print(emp2.emp_name)          # same with the emp2
                              # self = reference for obj we are creating  

#Difference between Class Variable and Instance Variable
