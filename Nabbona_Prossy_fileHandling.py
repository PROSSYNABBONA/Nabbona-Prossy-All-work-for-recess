# #We have to first open the file
# #f = open(file1, mode)
# """
# file modes
# r: open an existing file for a read operation.
# w: open an existing file for a write operation and If the file already contains some data then it will be overridden but if the file is not present then it creates the file as well.
# a:  open an existing file for append operation. It wont override existing data.
# r+:  To read and write data into the file. The previous data in the file will be overridden.
# w+: To write and read data. It will override existing data.
# a+: To append and read data from the file. It wont override existing data.

# """
# #Example 1: The open command will open the file in the read mode and the for 
# #loop will print each line present in the file.
# # a file named "Prossy.txt", will be opened with the reading mode.
file = open('Prossy.txt', 'r')
 
# This will print every line one by one in the file
for each in file:
    print (each)
    
#     #Python code to illustrate read() mode
file = open("Prossy.txt", "r")
print (file.read())
# #reading a file with "with" statement
with open("Prossy.txt") as file: 
    data = file.read()
print(data)
# #Reading a specific number of characters
# # Python code to illustrate read() mode character wise
file = open("Titi.txt", "r")
print (file.read(5))

# #We can also split lines while reading files in Python.
# # The split() function splits the variable . 
with open("Ruth.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print (word)
        
#  #creating file using the write()
file = open('Write1.txt','w')
file.write("This is the write command")
file.write("It allows us to write in a particular file")
file.close()  


#  #Write() and with 
with open("Write2.txt", "w") as f:
    f.write("Hello Prossy") 

# #Working with Append Mode
file = open('Write2.txt', 'a')
file.write("This will add a new  line of text")
file.close()

# #Deleting a file
# #To delete a file, you must import the OS module, and run its os.remove() function:
# #Combinding all the modes

# import os
# os.remove("Demo_delete.txt")

# #removing entire folder
# #only empty folders can be deleted

#os.rmdir("Folder") 
"""
rstrip(): It strips each line 
of a file off spaces from the right-hand side.
lstrip(): It strips each line of a 
file off spaces from the left-hand side

"""
import os

def create_file(file1):
	try:
		with open(file1, 'w') as f:
			f.write('Hello, world!\n')
		print("File " + file1 + " created successfully.")
	except IOError:
		print("Error: could not create file " + file1)

def read_file(file1):
	try:
		with open(file1, 'r') as f:
			contents = f.read()
			print(contents)
	except IOError:
		print("Error: could not read file " + file1)

def append_file(file1, text):
	try:
		with open(file1, 'a') as f:
			f.write(text)
		print("Text appended to file " + file1 + " successfully.")
	except IOError:
		print("Error: could not append to file " + file1)

def rename_file(file1, new_file1):
	try:
		os.rename(file1, new_file1)
		print("File " + file1 + " renamed to " + new_file1 + " successfully.")
	except IOError:
		print("Error: could not rename file " + file1)

def delete_file(file1):
	try:
		os.remove(file1)
		print("File " + file1 + " deleted successfully.")
	except IOError:
		print("Error: could not delete file " + file1)


if __name__ == '__main__':
	file1 = "example.txt"
	new_file1 = "new_example.txt"

	create_file(file1)
	read_file(file1)
	append_file(file1, "This is some additional text.\n")
	read_file(file1)
	rename_file(file1, new_file1)
	read_file(new_file1)
	delete_file(new_file1)
