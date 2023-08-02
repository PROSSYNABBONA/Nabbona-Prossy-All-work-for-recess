
"""
Types of exceptions
SyntaxError: This exception is raised when the interpreter encounters a syntax error in the code, such as a misspelled keyword, a missing colon, or an unbalanced parenthesis.
TypeError: This exception is raised when an operation or function is applied to an object of the wrong type, such as adding a string to an integer.
NameError: This exception is raised when a variable or function name is not found in the current scope.
IndexError: This exception is raised when an index is out of range for a list, tuple, or other sequence types.
KeyError: This exception is raised when a key is not found in a dictionary.
ValueError: This exception is raised when a function or method is called with an invalid argument or input,
such as trying to convert a string to an integer when the string does not represent a valid integer.
AttributeError: This exception is raised when an attribute or method is not found on an object, such as trying to access a non-existent attribute of a class instance.
IOError: This exception is raised when an I/O operation, such as reading or writing a file, fails due to an input/output error.
ZeroDivisionError: This exception is raised when an attempt is made to divide a number by zero.
ImportError: This exception is raised when an import statement fails to find or load a module.

Exception handling
The try block lets you test a block of code for errors.

The except block lets you handle the error.

The else block lets you execute code when there is no error.

The finally block lets you execute code, regardless of the result of the try- and except blocks.
"""
# years = 20
 
# # perform division with 0
# a = years / 0
# print(a)

#When an exception occurs  python
# generates an error message
#y=3
try:
     print(y)
except:
     print("An exception has occured")
#it print this error

a = [1, 2, 3]
try:
    print ("Second element = %d" %(a[1]))
 
    # Throws error since there are only 3 elements in array
    print ("Fourth element = %d" %(a[3]))
 
except:
    print ("An error occurred in this exception")
#Many exceptions python allows many exceptions
s=7
try:
  print(s)
except NameError:#This exception is raised when a variable or function name is not found in the current scope.
  print("Variable x is not defined")#It print this error
except:
  print("Something else went wrong") 

#Else is used to define a block of code to be excecuted
#if no errors were raised 
try:
  print("Hello Prossy")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong") #this wiill be printed
  
  #Handling multiple errors with one except statement
#   def fun(a):
#     if a < 3:
 
#         # throws ZeroDivisionError for a = 3
#         b = a/(a-2)
 
#     # throws NameError if a >= 4
#     print("Value of b = ", b)
     
# try:
#     fun(3)
#     fun(5)
 
# # note that braces () are necessary here for
# # multiple exceptions
# except ZeroDivisionError:
#     print("ZeroDivisionError Occurred and Handled")
# except NameError:
#     print("NameError Occurred and Handled")
  
 #Finally block will be excecuted 
 #will be executed regardless if the try block raises an error or not.
q=5
try:
  print(q)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
  
  #Raise an exception
   #One can choose to throw an error if a condition occurs
   #To throw (or raise) an exception, use the raise keyword.
# x = -1

# if x < 0:
#   raise Exception("Sorry, no numbers below zero")
#Exception will be raised with the message 
"Sorry, no numbers below zero" #if x is less than zero. and which is true
#One can also define what kind of error to raise
x = "hello Prossy"

if not type(x) is int:
  raise TypeError("Only integers are allowed")
"""
Type error 
This exception is raised when an operation
 or function is applied to an object
 of the wrong type, such as adding a string to an integer.
"""