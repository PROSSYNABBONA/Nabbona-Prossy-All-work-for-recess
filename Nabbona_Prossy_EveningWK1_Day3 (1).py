############# Exercise 1 LISTS#########
#  1: Output the 2nd item in the list
names_of_people = ["Prossy", "Bob", "Carol", "David", "Eve"]
print(names_of_people[1])

#  2: Change the value of the first item to a new value
names_of_people[0] = "Titi"
print(names_of_people)

#  3: Add a sixth item to the list
names_of_people.append("Wenini")
print(names_of_people)

# Task 4: Add "Bathel" as the 3rd item in the list
names_of_people.insert(2, "Bathel")
print(names_of_people)

# Task 5: Remove the 4th item from the list
del names_of_people[3]
print(names_of_people)

# 6: Print the last item in the list using negative indexing
print(names_of_people[-1])

#  7: Create a new list and print the 3rd, 4th, and 5th items using range of indexes
Fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grape"]
print(Fruits[2:5])

# 8: Make a copy of a list of countries
countries = ["USA", "UK", "Germany", "France", "Japan"]
countries_copy = countries.copy()
print(countries_copy)

# Task 9: Loop through the list of countries
for country in countries:
    print(country)

#  10: Sort a list of animal names in ascending and descending order
animal_names = ["Lion", "Tiger", "Elephant", "Giraffe", "Monkey"]
ascending_order = sorted(animal_names)
descending_order = sorted(animal_names, reverse=True)
print(ascending_order)
print(descending_order)

#  11: Output animal names with the letter 'a'
names_with_a = [name for name in animal_names if 'a' in name.lower()]
print(names_with_a)

# 12: Join two lists of first names and second names
first_names = ["Nabbona"]
second_names = ["Prossy"]
full_names = first_names + second_names
print(full_names)


####### Exercise 2 TUPLES#######
# Task 1: Output your favorite phone brand from the tuple
x = ("samsung", "iphone", "tecno", "redmi")
favorite_brand = x[0]
print(favorite_brand)

#  2: Print the 2nd last item in the tuple using negative indexing
second_last_item = x[-2]
print(second_last_item)

# 3: Update "iphone" to "itel" in the tuple
updated_tuple = list(x)
updated_tuple[1] = "itel"
x = tuple(updated_tuple)
print(x)

#  4: Add "Huawei" to the tuple
x = x+("Huawei",)
print(x)

#  5: Loop through the tuple
for phone in x:
    print(phone)

# Task 6: Remove the first item in the tuple
x = x[1:]
print(x)

#  7: Create a tuple of cities in Uganda using the tuple() constructor
uganda_cities = tuple(["Kampala", "Entebbe", "Jinja", "Mbarara"])
print(uganda_cities)

#  8: Unpack the tuple
city1, city2, city3, city4 = uganda_cities
print(city1, city2, city3, city4)

# Task 9: Print the 2nd, 3rd, and 4th cities using a range of indexes
print(uganda_cities[1:4])

# Task 10: Join two tuples of first names and second names
first_names = ("Nabbona")
second_names = ("Prossy")
full_names = first_names + second_names
print(full_names)

# Task 11: Create a tuple of colors and multiply it by 3
colors = ("red", "blue", "green")
multiplied_colors = colors * 3
print(multiplied_colors)

# Task 12: Count the number of times 8 appears in the tuple
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
count_of_8 = thistuple.count(8)
print(count_of_8)

########## Exercise 3 SETS######
#1
favorite_beverages = set(["coffee", "tea", "smoothie"])

# Print the set of favorite beverages
print("Favorite Beverages:", favorite_beverages)

#2 
favorite_beverages = set(["coffee", "tea", "smoothie"])

# Add two more items to the set
favorite_beverages.add("juice")
favorite_beverages.add("water")
print("Updated Set:", favorite_beverages)


#3 checking microwave
mySet = {"oven", "kettle", "microwave", "refrigerator"}
# Check if "microwave" is present in the set
if "microwave" in mySet:
    print("Microwave is present in the set")
else:
    print("Microwave is not present in the set")
    
    
#4 remove kettle
mySet = {"oven", "kettle", "microwave", "refrigerator"}
mySet.remove("kettle")
print("Updated Set:", mySet)


#5 looping trough
mySet = {"oven", "kettle", "microwave", "refrigerator"}
for item in mySet:
    print(item)
    
#6  Write a set of 4 items and a list of two items. Write a python program to add elements in 
#the list to elements in the set
mySet = {"apple", "banana", "orange", "grape"}
myList = ["strawberry", "kiwi"]
mySet.update(myList)
print("Updated Set:", mySet)

#7Write two sets, one containing your ages and the other your first names. Join the two sets
ages = {25, 30, 35, 40}
first_names = {"John", "Emma", "Michael", "Olivia"}
combined_set = ages.union(first_names)
print("Combined Set:", combined_set)

  ######### Exercise 4 Strings########
  
  #1. Declare an integer and a string variable
my_int = 10
my_string = "Hello"
concatenated_string = my_string + " " + str(my_int)
print(concatenated_string)


###2.removing spaces
txt = " Hello, Uganda! "
# Remove spaces at the beginning using strip()
trimmed_txt = txt.strip()
# Remove spaces in the middle using replace()
trimmed_txt = trimmed_txt.replace(" ", "")
# Print the trimmed string
print(trimmed_txt)


## 3. to upper case
txt = "Hello, Uganda!"
# Convert the value to uppercase using the upper() method
txt_upper = txt.upper()
# Print the uppercase string
print(txt_upper)

#4.
txt = "Hello, Uganda!"
#  Replace 'U' with 'V' using the replace() method
txt_replaced = txt.replace('U', 'V')
# Print the replaced string
print(txt_replaced)

#5.
y = "I am proudly Ugandan"
#. Get the range of characters using indexing
character_range = y[1:4]
# Print the range of characters
print(character_range)

#6The piece of code below will give an error when output;
#x = “All “Data Scientists” are cool!”
#Write a python program to correct it.
x = 'All "Data Scientists" are cool!'
print(x)


######## Exercise 5 DICTIONARIES########
# Define the Shoes dictionary
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

# 1. Print the value of the shoe size
print("Shoe Size:", Shoes["size"])

# 2. Change the value "Nick" to "Adidas"
Shoes["brand"] = "Adidas"

# 3. Add a key/value pair "type": "sneakers" to the dictionary
Shoes["type"] = "sneakers"

# 4. Return a list of all the keys in the dictionary
keys_list = list(Shoes.keys())
print("Keys:", keys_list)

# 5. Return a list of all the values in the dictionary
values_list = list(Shoes.values())
print("Values:", values_list)

# 6. Check if the key "size" exists in the dictionary
if "size" in Shoes:
    print("Key 'size' exists in the dictionary")
else:
    print("Key 'size' does not exist in the dictionary")

# 7. Loop through the dictionary
for key, value in Shoes.items():
    print(key, ":", value)

# 8. Remove "color" from the dictionary
Shoes.pop("color")

# 9. Empty the dictionary
Shoes.clear()

# 10. Create a dictionary and make a copy of it
myDict = {"name": "Prossy", "age": 22}
copyDict = myDict.copy()

# Print the copy dictionary
print("Copy Dictionary:", copyDict)

#11
# Define a nested dictionary
students = {
    "stud1": {
        "name": "Prossy",
        "age": 20,
        "grade": "A"
    },
    "student2": {
        "name": "Lydia",
        "age": 22,
        "grade": "B"
    },
    "student3": {
        "name": "Winnie",
        "age": 19,
        "grade": "A"
    }
}

# Access and print the values in the nested dictionary
for student_id, student_info in students.items():
    print("Student ID:", student_id)
    print("Name:", student_info["name"])
    print("Age:", student_info["age"])
    print("Grade:", student_info["grade"])
    print()






