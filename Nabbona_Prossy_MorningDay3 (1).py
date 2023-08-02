#Day3
#Basic operaters and expressions(input and output opreator)
"""
#Arithmetic operators
+Addiction
-subtraction
*multiplication
/division
%Modulus
** Exponentiation
//floor division

#comparison operator
== equal to
!=not equal !==
>greater than
< less than
>greater than or equal to
<=less than or equal to

#logical operators
Logical AND 'and'
Logical OR 'or'
Logical NOT 'not'

#Assignment operators
Assign value: '='
Add  value: '+'
Add and assign value: '+='
subtract and assign value: '-='
Modulus and assign value: '%='
Exponetiate and assign value: '**='

#Membership operators
In :'in' checks if a value exists in asequence
Not in: 'not in' checks if valus doesnot exit in a sequence
Is not: 'is not' checks if two values are not the same

"""

# #Examples
# #Addition
# x=50+36
# print(x)
# #Subtraction
# y=50-36
# print(y)
# #Divide
# q=50/2
# print(q)
# #Division
# z=50//36
# print(z)
# #Modulus
# w=50%36
# print(w)
# #Exponentiation
# g=50**2
# print(g)

# #Examples of comparision opretors
# a=15
# b=9
# #Greater than
# if a>b:
#     print('a is greater than b')
#     print(a>b)
# #Less than 
# if a<b:
#     print('a is less than b')
#     print(a<b) 
# #greater than or equal to
# if a>=b:
#     print('a is greater than  or equal to b')
#     print(a>=b)  
# #less than or equal to
# if a<=b:
#     print('a is less than b')
#     print(a<=b)    
    
#  #Equal to
# if a==b:
#      print('a is equal to b')
#      print(a==b)   
# #Not equal to
# if a !=b:
#     print('a is not equal to b')
#     print(a != b)
# #Less than or equal ti
#     print(a<=b)
# #Equal to
#     print (a==b)
    
#logical operators
#Examples with logical operator
# a= True
# b=False

# #Logical AND
# print(a and b)

# #logical OR
# print (a or b)

# #Logical NOT
# print(not a)
# print(not b)
    
 #Assignment operators
a=5 
#Add and assign
# a+=5
# print(a) 
# #subtract and assign
# w=3
# w-=5
# print(w)
# #multiply and assgn
# d= 19
# d*=3
# print(d)
# #divide and assign
# v= 19
# v/=3
# print(v)
# #Modulus and assign
# q= 19
# q%=3
# print(q)
# #Exponential and assign
# t= 19
# t**=3
# print(t)
# #Membership operator
# cars=['Jeep','Benz','BMW']
# if 'Jeep' in cars:
#     print('Jeep is in the list')
#     print('Benz' in cars)
#     print('BMW' in cars)
    
 #Identity operrateors   
# x=10
# y=10
# #is operator
# print(x is y)
# print(x is not y)
# print(x==y)
# print(x!=y)
# print(x<y)
# print(x<=y)
#  #List
#  # #is not operator
 
# z=[1,2,3,4,5,6,7]
# w=[1,2,3,4,5,6,7]
# print(z is not  w)

#Bitwise operators
"""
They are used to perform operations on individual bits in of binary numbers
Bitwise AND('&'):Performs a bitwise AND operation between the corresponding bits of two intergers
Bitwise OR('|')
Bitwise XOR('^')
Bitwise Not('~')
bitwise left shift('<<')
Bitwise right shift('>>')


"""
#Examples of Bitwise
# a=10
# b=20
# #Bitwise AND opreations
# result_and = a & b
# print(result_and)

# #Bitwise or
# result_or = a | b
# print(result_or)


# #bitwise not
# result_and = a & b
# print(result_and)

# #bitwise XOR
# result_and = a XOR b
# print(result_and)

# #bitwise  left shift
# result_left = a << b
# print(result_left)

# #bitwise right shift
# result_right= a >> b
# print(result_right)

#Example an assign
#Create a simple calculator function to calculate(add, subtract,multiply,divide)
# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     return a / b

# def main():
#     print('Prossy simple calculator')
#     Num1 = float(input("Enter the first number: "))
#     Num2 = float(input("Enter the second number: "))
#     operator = input("Enter the operator (+, -, *, /): ")
    
#     if operator == '+':
#         result = add(Num1, Num2)
#     elif operator == '-':
#         result = subtract(Num1, Num2)
#     elif operator == '*':
#         result = multiply(Num1, Num2)  
#     elif operator == '/':
#         result = divide(Num1, Num2) 
#     else:
#         print('Invalid operator')
#         return
    
#     print("The result is", result)

# if __name__ == '__main__':
#     main()

####################CALCULATOR############################    
     
         #learn tkinter
         #Assignmement 1:create a simple calculator program with a GUI interface
         #Make the title of the calculater program with your name eg Nabbona Prossy simple calculator


import tkinter as tk

# Create a new Tkinter window
window = tk.Tk()
window.title("Nabbona Prossy Simple Calculator")

# Function to perform the calculation
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operator = operator_var.get()

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            result = num1 / num2

        result_label.config(text=" The Result is: " + str(result))
    except ValueError:
        result_label.config(text="Invalid input,please try again")

# Create input fields
entry1 = tk.Entry(window)
entry1.pack()

operator_var = tk.StringVar(window)
operator_var.set("+")  # Default operator

operator_dropdown = tk.OptionMenu(window, operator_var, "+", "-", "*", "/")
operator_dropdown.pack()

entry2 = tk.Entry(window)
entry2.pack()

# Create calculate button
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.pack()

# Create label for displaying the result
result_label = tk.Label(window)
result_label.pack()

# Start the Tkinter event loop
window.mainloop()
      
           
    


