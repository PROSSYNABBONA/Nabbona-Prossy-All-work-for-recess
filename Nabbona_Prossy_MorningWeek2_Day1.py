#object oriented programming
"""
classes
objects
encapsulation
inheritance
polymormorphism
abstraction
"""
#Class
#Aclass is a blueprint for creating objects
# #Example
# class Car:
#     def__init__(self,make,model,year):
#         self.make=make
#         self.model=model
#         self.year=year
        
#         def start_engine(self):
#             print("Engine started")
            
#         def stop_engine(self):
#             print("Engine stopped") 
            
# my_car=  Car("toyota","Corolla",2023)
# print(my_car.make)
# print(my_car.model)
# print(my_car.year)
# my_car.start_engine()
# my_car.stop_engine()

# #Example:Rectagle 
# class Rectangle:
#     def __init__(self,length,width):
#         self.length=length
#         self .width=width
         
#     def area (self):
#         return self.length*self.width  
#     def perimeter (self):
#         return 2*(self.length+self.width )
# my_rectangle=Rectangle(10,5) 
# #calculate and display area and primeter
# print(my_rectangle.area())
# print(my_rectangle.perimeter)  
        
  #UNiversity student
# class Student:
#   def __init__(self,name,year,course):
#       self.name=name
#       self.year=year
#       self.course=course
      
#   def display_details(self):
#       print("Name:",self.name)
#       print("Year:",self.year)
#       print("Course:",self.course)    
      
#       #create a student object
      
# my_student=Student("Nabbona Prossy",3,"software engineering")
#     #Display my details
# my_student.display_details()


#Object
# class Person:
#     def __init__(self,name,age):
#         self.name=name=name
#         self.age=age
        
#     def greet(self):
#         print("Hello",self.name) 
#         print("I am",self.age,"years")
#         #create a person object
#         my_person=Person("Prossy",22)   
#         my_person=Person("Morren",23)
        
#         #Accessing attributes
#         print(my_person.name)
#         print(my_person.age)
      
      
      
      
      
      
      #Exercise 1:Calculate the area  and perimeter of a rectangle  
# class Rectangle:
#     def __init__(self,length,width):
#         self.length=length
#         self .width=width
         
#     def area (self):
#         return self.length*self.width  
#     def perimeter (self):
#         return 2*(self.length+self.width )
# my_rectangle=Rectangle(10,5) 
# #calculate and display area and primeter
# print(my_rectangle.area())
# print(my_rectangle.perimeter)  
      
      #Exercise 2:calculate and display  employee bonus (15%) of salary (employee1:150000,employee2:230000)
# class Employee:
#      def __init__(self, name, salary):
#         self.name = name 
#         self.salary = salary
        
#      def cal_bonus(self):
#         return self.salary * 0.15
    
#      def display_details(self):
#         print("Name:", self.name)
#         print("Salary:", self.salary)
#         print("Bonus:", self.cal_bonus())

# Creating objects
# emp1 = Employee("Prossy Nabbona", 150000)
# emp2 = Employee("Morren", 230000)

# emp1.display_details()
# emp2.display_details()


#Encapsulation
#key goal of encapsulation is to
"""
To hide the implementation the implementation of an object

"""
#Examples
# class BankAccount:
#     def __init__(self, account_number, balance):
#         self.account_number = account_number  # encapsulates the account number attribute
#         self.balance = balance  # encapsulates the balance attribute

#     def deposit(self, amount):
#         self.balance += amount

#     def withdraw(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#         else:
#             print("Insufficient funds")

#     def get_balance(self):
#         return self.balance


# # Create BankAccount object
# my_account = BankAccount("1245664766", 1000)

# # Accessing the BankAccount object
# print(my_account.account_number)
# print(my_account.balance)

# my_account.deposit(500)
# print(my_account.balance)

# my_account.withdraw(100)
# print(my_account.balance)

  
  #Exercise 2:convert temperature(37 Celsius) to Fahrenherit 
  #and try to encapsulate the data  
# class Temperature:
#     def __init__(self, _celsius):
#         self.celsius = _celsius
#     #This method is responsible for converting a 
#     # temperature value in Celsius to Fahrenheit
#     def to_fahrenheit(self):
#         fahrenheit = (self.celsius * 9/5) + 32
#         return fahrenheit

# # Creating a Temperature object
# temp = Temperature(37)

# # Converting Celsius to Fahrenheit
# fahrenheit_temp = temp.to_fahrenheit()

# print("Temperature in Celsius:", temp.celsius)
# print("Temperature in Fahrenheit:", fahrenheit_temp)

#Assignment 2:
#Show encapsulation with employee information to give a pay increamentation(salary with employee information
# to new salary) eg from 850000 to 1000000
class Employee:
    def __init__(self, _name, _salary):
        self._name = _name
        self._salary = _salary

    def get_name(self):
        return self._name

    def get_salary(self):
        return self._salary

    def set_salary(self, new_salary):
        if new_salary > self._salary:
            self._salary = new_salary

    def give_raise(self, increment):
        if increment > 0:
            self._salary += increment


# Creating an Employee object
employee = Employee("Nabbona Prossy", 850000)

# Getting the current salary
current_salary = employee.get_salary()
print("Current Salary:", current_salary)


# Give a raise
increment = 150000
employee.give_raise(increment)
print("New Salary after Raise:", employee.get_salary())
        


            