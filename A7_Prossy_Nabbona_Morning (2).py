#Context Manager-is an object that defines a temparary context for a block of code
#Example1:
#demostrating acontext manager to open a file and retuns a context manager instance
# def open_file(filename):
    
#    #open a file and return a context manager instance
#  file=open(filename,"r")
# def __enter__():
#         return file
    
# def __exit__(self,exc_type, exc_value, exc_tb):
#         file.close()
        
#         return __enter__, __exit__
    
# with open_file("my_file.txt") as f:
#     contexts=f.read()
    #benefits sif context managers
"""
    code more readable
    avoiding common errors
    more efficient code
    """
   #Example 2 :Demostrate a context manager using a time series
# import time

# class Timer:
#     def __enter__(self):
#         self.start_time = time.time()
#         return self

#     def __exit__(self, exc_type, exc_value, traceback):
#         end_time = time.time()
#         execution_time = end_time - self.start_time
#         print(f"Execution time: {execution_time} seconds elapsed")

# # Example usage
# # Measures execution time
# with Timer():
#     time.sleep(2)
#     print("Hello Prossy")
    
    #Multithreading and multiprocessing
"""
        They are techiques that can be use dtho improve perfomance of a python progarm
        """
        #Multithreading:Is a technique where multiple threads are created with in a single processs
        #Multiprocessing:Is a technique where multiple processes are created.
        
    #     #Example3 of multithreading
    # import threading
    
    # def task(name):
    #     print(f"Running task {name}")
    # #create multiple threads
    # threads=[]
    # for i in range(5):
    #     t=threading.Thread(target=task, args=(f" Thread {i}" ,))
    #     threads.append(t) 
    #     t.start() 
        
    #     #Wait for the therads to finish before we join
    #     for t in threads:
    #         t.join()
        
        #Example 4 of multiprocessing  

#Example 5
#Demonstarating use of multithraeding and multiprocessing

# import multiprocessing
# import threading

# def task(name):
#     print(f"Running task {name} on thread {threading.current_thread().name} with process {multiprocessing.current_process().name}")

# threads = []

# for i in range(4):
#     t = threading.Thread(target=task, args=(f"Thread {i}",))
#     threads.append(t)
#     t.start()

# # Wait for all threads to finish
# for t in threads:
#     t.join()
    
    #Assignment A7:
#1a) Show a context manager for file handling that automatically opens and closes a file.
class Prossy:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()

 #usage
with Prossy("Prossy.txt", "r") as f:
    contents = f.read()
    print(contents)
    

#b) Shows a context manager for managing a database connection.
import sqlite3

class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_name)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()

# database name
db_name = "Prossy_database.db"

# Using the context manager
with DatabaseConnection(db_name) as db:
    cursor = db.cursor()
    # Create the "people" table if it doesn't exist
    cursor.execute("CREATE TABLE IF NOT EXISTS people (id INTEGER PRIMARY KEY, name TEXT)")
    
    # Insert a sample user
    cursor.execute("INSERT INTO people (name) VALUES ('Nabbona Prossy')")
    db.commit()

    # Performing database operations on people
    # The first line of code creates a cursor object that allows you to execute SQL statements and fetch 
    # results from the database.
    cursor.execute("SELECT * FROM people")
    results = cursor.fetchall()
    for row in results:
        print(row)




#c) Show a multithreading and multiprocessing  that allows us to run the function for different amounts of time.
import time
import threading
import multiprocessing

# Function that takes a duration parameter and prints a message
def my_function(duration):
    print(f"Starting function with duration {duration} seconds...")
    time.sleep(duration)
    print(f"Function with duration {duration} seconds completed.")

# Multithreading example
def multithreading_example():
    # List of durations for the function
    durations = [3, 5, 2, 4]

    # Create and start a thread for each duration
    threads = []
    for duration in durations:
        thread = threading.Thread(target=my_function, args=(duration,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    print("Multithreading example completed.")

# Multiprocessing example
def multiprocessing_example():
    # List of durations for the function
    durations = [3, 5, 2, 4]

    # Create and start a process for each duration
    processes = []
    for duration in durations:
        process = multiprocessing.Process(target=my_function, args=(duration,))
        processes.append(process)
        process.start()

    # Wait for all processes to complete
    for process in processes:
        process.join()

    print("Multiprocessing example completed.")

if __name__ == "__main__":
    # Run the examples
    multithreading_example()
    print()
    multiprocessing_example()
