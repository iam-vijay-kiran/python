### Static Method ###

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


## print instance variables of a object
print(emp1.emp_name)
print(emp1.emp_salary)
print(emp2.emp_name)
print(emp2.emp_salary)


## lets access class variable from instance itself
print(emp1.empCount)
print(emp2.empCount)

# explicetly trying to change empCount values which can be accessed
emp1.empCount = 10
emp2.empCount = 20         

print(emp1.empCount)
print(emp2.empCount)  # here the change of output is only for this instance 

# But, when we try to change empCount from class name

print(Employee.empCount)   # it shows the value which is tightely coupled with the class as global change


### What is Static Method
## without creating the object and its references we can directly call values 
# which are inside static method

class Car:

    def __init__(self, name, color):
        self.car_name = name
        self.car_color = color

    def displayCarDetails(self):
        print("Car name is",self.car_name,"and Car color is ",self.car_color)
    
    @staticmethod
    def initialMessage():
        print("Nice Car !!!!!")

 
Car.initialMessage()         # works without passing values when called as it is static method
car1 = Car('XUV 700', 'Red')     
car1.displayCarDetails()     # works only when values are passed, then called as it is not static

## for example here we are calling without passing value to not static method which doesn't work
## and throws an error

# Car.displayCarDetails()

class Calculation:
    @staticmethod
    def add2Nums(num1, num2):
        print("Sum of two numbers = ", num1 + num2)
    
Calculation.add2Nums(2,7)
