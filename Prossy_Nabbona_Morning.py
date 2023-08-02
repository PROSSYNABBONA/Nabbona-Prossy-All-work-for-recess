# class Animal:
#     def __init__(self,name):
#         self.name=name
#         def eat (self):
#             print(f"{self.name} is eating ....")
            
# class Dog(Animal):
#     def bark(self):
#         print(f"{self.name} is barking...")            

# class Cat(Animal):
#  def memw(self):
#     print(f"{self.name} is memewing....f")
    
# #create animal objects
# animal =Animal("Good Animal")
# dog=Dog("Spot")    
# cat= Cat("flutty")
# #invoking
# animal.eat()
# dog.eat()
# cat.eat()

#Example 2
# class Vehicle:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color

#     def display_info(self):
#         print("Brand:", self.brand)
#         print("Color:", self.color)

#     def move(self):
#         print("Moving the vehicle...")


# class Car(Vehicle):
#     def __init__(self, brand, color, num_wheels):
#         super().__init__(brand, color)
#         self.num_wheels = num_wheels

#     def honk(self):
#         print("Honking the horn...")


# # Create a car object
# my_car = Car("Toyota", "Red", 4)

# print("Brand:", my_car.brand)
# my_car.color = "Blue"

#Exercise1:Demonstrate using inheritance to calculate the area
# and perimeter of a crrcle and rectangle respectively(Shape:circle)
# import math

# class Shape:
#     def area(self):
#         pass

#     def perimeter(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * self.radius**2

#     def perimeter(self):
#         return 2 * math.pi * self.radius

# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

#     def perimeter(self):
#         return 2 * (self.length + self.width)

# # Example usage:
# circle = Circle(5)
# print("Circle Area:", circle.area())
# print("Circle Perimeter:", circle.perimeter())

# rectangle = Rectangle(4, 6)
# print("Rectangle Area:", rectangle.area())
# print("Rectangle Perimeter:", rectangle.perimeter())

#Multiple inheritance
# class Animal:
#     def __init__(self,name):
#         self.name=name
        
#         def eat(self):
#             print(f"{self.name} is eating....")
           
#         class Flayable:
#                def fly(self):
#                    print(f"{self.name} is flying....") 
#          #this is multiple inheriance          
#         class Bird(Animal,Flayable): 
#             def __init__(self,name,species):
#                 super().__init__(name)
#                 self.species=species   
                
#                 def display_info(self):
#                     super().display_info()
#                     print(f"Species:{self.name}")
#                     print(f"Name:{self.name}")
                    
#                     my_bird= Bird("Pig","Bird")
                    
#                     my_bird.eat()
#                     my_bird.fly()
#                     #my_bird.display_info()
                    
                    
#                     #Method Overridings
#                     class Animal:
#                         def make_animal_sound(self,name):
#                            print("Animal is making a sound")
                           
#                     class Dog(Animal):
#                          def make_animal_sound(self): 
#                              print("Dog is making a baking")
#                     class Cat(Animal):
#                         def make_animal_sound(self):  
#                             print("Cat is meaowing")
                            
#                         def make_animal_sound(animal):
#                             animal.make_sound()
                            
#                             #creating objects
#                             animal=Animal()
#                             dog=Dog()
#                             cat=Cat()  
                            
#                             #calling make_animal_sound function
#                             # make_animal_sound(animal)
#                             # make_animal_sound(dog)
#                             # make_animal_sound(cat)                                          
                                                    

#POLYMORPHISM

#Allows u to write code that can work with different objects
#Method Overriding occurs wen a deirived class provides its own implemenation of the method that is already diffied in its subclasses
#which is alredy difined in its base class

#Method overloading allows a class to have multiple methods with the same name
#but different parameters

#Examples
# class Shape:
#     def calculate_area(self):
#         pass
# class Rectangle(Shape):
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
        
#         def calculate_area(self):
#             return length*self.width  
        
#     class Circle(Shape):
#      def __init__(self,radius):
#         self.radius=radius
        
#     def calculate_area(self):
#         return 3.14* self.radius**2 
    
#     def calculate_circumfrace(self):
#         return 2*3.14* self.radius
#     #crate shape objects
#     rectangle=Rectangle(4,6)
#     circle=Circle(5)
    
#     #calculate display area
#     print(" Rectangle", rectangle.calculate_area())
#     print("Circle area",circle.calculate_area())
    
# class Shape:
#     def calculate_area(self):
#         pass

# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def calculate_area(self):
#         return self.length * self.width

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def calculate_area(self):
#         return 3.14 * self.radius**2

#     def calculate_circumference(self):
#         return 2 * 3.14 * self.radius

# # Create shape objects
# rectangle = Rectangle(4, 6)
# circle = Circle(5)

# # Calculate and display area
# print("Rectangle area:", rectangle.calculate_area())
# print("Circle area:", circle.calculate_area())

  #Overlodding functions
# class Calculator:
#       def add(self,x,y):
#           return x+y
#       def add (self,x,y,c):
#           return x+y+c
      
#       cal=Calculator()
      
#       print(cal.add(1,2))
#       print(cal.add(1,2,3))
      
      
      #Abstraction
      #Allows u to focus on essential features and hide them from necessary details
#       #Examples
# from abc import ABC,abstractmethod

# class Vehicle(ABC):
#     #abstract
#     def start(self):
#         pass
#     #abstract
#     def stop(self):
#         pass
    
#     class Car(Vehicle):
#         def start(self):
#             print("Started the car")
#         def stop(self):
#             print("Stopped the car") 
#     class Truck(Vehicle):
#         def start(self):
#             print("Started the truck")
            
#         def stop(self):
#             print("Stopped the truck") 
            
#         #Objects       
#         car=Car()
#         truck=Truck()
#         #for starting
#         car.start()
#         truck.start() 
#         #for stopping
#         car.stop()
#         truck.stop()       
        
#         #Exercise 2    
        
        # Demonstrate abstraction while calculating
        # area of a circle and rectangle                      
# from abc import ABC, abstractmethod
# import math

# class Shape(ABC):
#     @abstractmethod
#     def calculate_area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def calculate_area(self):
#         return math.pi * self.radius ** 2

# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def calculate_area(self):
#         return self.length * self.width

# # Create shape objects
# circle = Circle(5)
# rectangle = Rectangle(4, 6)

# # Calculate and display area
# print("Circle area:", circle.calculate_area())
# print("Rectangle area:", rectangle.calculate_area())

#Prossy_Nabbona_morning.py
#Prossy_Nabbona_afternoon.py
#Assignment 1:Deadline 1/07/2023 at 5pm
#create a receipt printing program GUI interface,a more advanced detail earns you more points
import tkinter as tk
from tkinter import messagebox

class ReceiptPrinterGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Nabbona Prossy's SuperMarket")

        # Create GUI elements
        self.label_item = tk.Label(self.window, text="Item:")
        self.label_item.pack()
        self.entry_item = tk.Entry(self.window)
        self.entry_item.pack()

        self.label_quantity = tk.Label(self.window, text="Quantity:")
        self.label_quantity.pack()
        self.entry_quantity = tk.Entry(self.window)
        self.entry_quantity.pack()

        self.label_price = tk.Label(self.window, text="Price:")
        self.label_price.pack()
        self.entry_price = tk.Entry(self.window)
        self.entry_price.pack()

        self.button_add = tk.Button(self.window, text="Add Item", command=self.add_item)
        self.button_add.pack()

        self.scrollbar = tk.Scrollbar(self.window)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.receipt_text = tk.Text(self.window, height=10, width=70)
        self.receipt_text.pack()
        self.receipt_text.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.receipt_text.yview)

        self.label_subtotal = tk.Label(self.window, text="Subtotal:")
        self.label_subtotal.pack()
        self.label_subtotal_value = tk.Label(self.window, text="shs 0.00")
        self.label_subtotal_value.pack()

        self.label_tax = tk.Label(self.window, text="Tax (5%):")
        self.label_tax.pack()
        self.label_tax_value = tk.Label(self.window, text="shs 0.00")
        self.label_tax_value.pack()

        self.label_total = tk.Label(self.window, text="Total:")
        self.label_total.pack()
        self.label_total_value = tk.Label(self.window, text="shs 0.00")
        self.label_total_value.pack()

        self.button_print = tk.Button(self.window, text="Print Receipt", command=self.print_receipt)
        self.button_print.pack()

        # Initialize variables
        self.items = []
        self.subtotal = 0.0

    def add_item(self):
        item = self.entry_item.get()
        quantity = self.entry_quantity.get()
        price = self.entry_price.get()

        if item and quantity and price:
            try:
                quantity = int(quantity)
                price = float(price)
            except ValueError:
                messagebox.showerror("Error", "Please enter valid quantity and price.")
                return

            item_total = quantity * price
            self.items.append((item, quantity, price, item_total))
            self.subtotal += item_total

            self.update_receipt()

            # Clear input fields
            self.entry_item.delete(0, tk.END)
            self.entry_quantity.delete(0, tk.END)
            self.entry_price.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter item, quantity, and price.")

    def update_receipt(self):
        self.receipt_text.delete("1.0", tk.END)
        for item in self.items:
            item_text = f"{item[0]} ({item[1]} x shs {item[2]:.2f}) = shs {item[3]:.2f}"
            self.receipt_text.insert(tk.END, item_text + "\n")
        self.receipt_text.insert(tk.END, "\n")

        self.label_subtotal_value.config(text=f"shs {self.subtotal:.2f}")

        tax = self.subtotal * 0.05
        self.label_tax_value.config(text=f"shs {tax:.2f}")

        total = self.subtotal + tax
        self.label_total_value.config(text=f"shs {total:.2f}")

    def print_receipt(self):
        receipt_text = self.receipt_text.get("1.0", tk.END)
        if receipt_text:
            messagebox.showinfo("Receipt: Thanks  for shopping with us", receipt_text)
        else:
            messagebox.showerror("Error", "No items to print.")

    def run(self):
        self.window.mainloop()

# Create an instance of the ReceiptPrinterGUI class and run the program
receipt_printer = ReceiptPrinterGUI()
receipt_printer.run()
