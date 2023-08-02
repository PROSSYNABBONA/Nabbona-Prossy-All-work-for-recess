#Dictionaries
#Used to store data values in key:values pairs
#They are ordered,chachable,dont allow duplicates
#They can be of different datatype
myDic={
    "phone":"iphone",
    "phonemodel":"iphone",
    "year": 2023
}
print(myDic)
#Lenght of a dictionary

print(len(myDic))
#Knowing datatype

print(type(myDic))
#Acessing Dictionary items,here we dont we indexes
z=myDic["year"]
print(z)

y=myDic.get("phonemodel")
print(y)
#accessing the keys eg year,phone
w=myDic.keys()
print(w)

#Exercise 1:use the values() method to return a list of all values in the dictionary
#Solution
#values() returns  a view object,the view object contains the values of the dictionary,as a list
Person={
    "Country":"Ugandan",
    "Religion":"Catholic",
    "Date_Of_Birth":"2007"
}
x=Person.values()
print(x)
#Exersice 2:check if a key exists in a dictionary
dict = {"a": 1, "b":2, "c":3}
if "a" in dict:
    print("Exists")
else:
    print("Does not exist")
#Exercise 3:give an example on how to change dictionary items,how to update,how to add an element
#changing dictionary item
Car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
Car["year"] = 2018
print(Car)

#updating an item
Car_Stuff =	{
  "brand": "Benz",
  "model": "Fordk",
  "year": 1964
}
Car_Stuff.update({"year": 2023}) 
print(Car_Stuff)

#Exercise 4:give an example on how to add dictionary items,how to remove an item
#how to add an item
#adding an item
dict1 =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dict1["color"] = "red"
print(dict1)
#removing an item
Fruits =	{
  "color": "green",
  "size": "big",
  "amount": 2
}
Fruits.pop("size")
print(Fruits)
#Exercise 5:give an example on how we can loop through a dictionary and how to nest dictionaries
#How to loop through dictionaries
#loop through using a for loop
fruits =	{
  "color": "green",
  "size": "big",
  "amount": 2
}
for x in fruits:
  print(x)  
  #how to nest dictionaries
  myfam = {
  "baby1" : {
    "name" : "Lydia",
    "year" : 2004
  },
  "baby2" : {
    "name" : "Carol",
    "year" : 2007
  },
  "baby3" : {
    "name" : "Martin",
    "year" : 2011
  }
}
 
# Accessing elements in nested dictionaries
# We use the name of the dictionary starting with the outer dictionary
print(myfam["baby1"]["name"])
print(myfam["baby2"]["name"])
print(myfam["baby3"]["name"])

#NUMBERS
#Numbers
#intergers,floats,complex
w=10#int
r=3.6#float
s=2j#complex

print(type(w))
print(type(r))
print(type(r))

#intergers
a=2
b=3456
c=-23442
print(type(a))
print(type(b))
print(type(c))

#floats
q=2.45
z=3.8
f=-78.8
print(type(q))
print(type(z))
print(type(f))

#complex numbers
s=2+10j
t=4j
h=-2j
print(type(s))
print(type(t))
print(type(h))

#Type conversion
#convert from int to complex
z=complex(w)
print(z)
print(type(z))
#convert from int to float
d=float(w)
print(d)
print(type(d))
#convert from float to complex
k=complex(q)
print(k)
print(type(k))
#convert from complex to float
t =  1+4j
h = t.real#real used to convert complex number to a float
print(h)
print(type(h))
 #STRINGS
 #Strings
print("Fruits")
print('Fruits')

#Assign string to a variable
w="Fruits"
print(w)
#Multiline strings
q="""I am a Software engineer,year 2
learning recess
    """
print(q)
#Strings as arrays
a="Prossy"
print(a[1])#outputs r because it is at position 1

#Exercise 1:use the len()function to determine the length of the string
#Length of a string
b="Hello, Prossy!"
print(len(b))
#Execise 2:Give an example of using a for loop in a string
Person = "Prossy"
for x in Person:
  print(x)

#Exercise 3:Give an example of slicing in strings
#Slicing helps to return arange of using a slice syntax
w="Hello"
print(w[2:5])
#how to modify strings
a="Cars"
print(a.lower())
print(a.upper())

#Remove white space
b=" Afternoon "
print(b.strip())#removes spaces at the beginning and end
#String concantination
c="Class"
d="chair"
w=c+ " " + d
print(w)

#Format_Strings
#Format string
#Works when you want to combine astring and a number
age=23
name="My name is Prossy and my age is {} "

print(name.format(age))

#Casting
#Casting
h=int(20)
y=int(3000)
a=int("8")# a is 8
print(h)
print(y)
print(a)
print(type(a))

#Boolean
#Booleans
print(10<5)
print(60==20)
print(40>10)

r="Prossy"
z=30
print(bool(r))
print(bool(z))
#Exercise use a condition to show how to use booleans
x = 6
y = 15
is_greater = x > y
is_equal = x == y

if is_greater:
    print("x is greater than y")
elif is_equal:
    print("x is equal to y")
else:
    print("x is less than y")



 
 
 
 




