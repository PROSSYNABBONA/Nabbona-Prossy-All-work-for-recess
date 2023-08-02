#if statements
a=22
b=33
if b>a:
    print("b is graeter than a")
    #Elif=means if the previous conditions were not true,then try this condition
    a=33
    b=33
    if b>a:print("b is greater than a")
    elif a==b:
        print("a and b are equal")
     #Else=catches anything which isnt caught by the preceeding conditions
    x=200
    y=33
    if y>x:
        print("y is greater than x")
    elif a==b:
        print("x and y are equal")
    else:
        print("x is greater than y")
#And
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
  
#Or
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")    
        


#loops(for,while)
#for loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  
#While loop example 1
fruits=["Apple","Mango","Orange","Grapes"]
fruit_count=0
while fruit_count<len(fruits):
    print(fruits[fruit_count])
    fruit_count +=1
    
#Example2 while loop
i=1
while i<6:
    print(i)
    i +=1
#  Break and continue statements
#Breaks are use within the loops
#And the are used to stop
for number in range(1,10):
    if number ==5:
        break 
    print(number)
    #Another example of break
    i=1
    while i<6:
        print(i)
        if i==3:
            break 
        i+=1
        
        #continue statement
        #We can stop the current iteration and continue with the next
    i=0
    while i<6:
        i+=1
        if i == 3:#This means i will skip the 3 and continue
            continue
        print(i)
        #Exception handling(try,except,finally)
        """
        
        Try block:we use it when raising an exception
        except:
        finally
        """
        try:
            x=10/0
        except ZeroDivisionError:
            print("Error: Division by zero")
        finally:
            print("This is always excecuted")
            
            #another example of exception
            try: 
                print(x)
            except:
                print("Someting went wrong")
            finally:
                print("The try except is finished")
                
                #Example
                #Dict is a dictionary{}
#                 emotion ={
#                     'happy':'I am glad to hear you are happier',
#                     'sad':'Im sorry taht yoy are sad',
#                     'angry':"Take a break",
#                     'fearful':"Stop feraing",
#                     'disgusted':"Do u feel disgusted"
#                 }
#                     #User enter ther emotions
# user_emotion=input("How are u feeling")
#                     #Convert the user input to lower case
# user_emotion=user_emotion.lower()
# if user_emotion in emotion:
#                         print(emotion(user_emotion))
# else:
#                         print("I am sorrry i dont understand emotions")
                    
                
      # Exercise 1
    #Write program to ask students about their metal health
    #Prompt students on a scale of 1 to 10 to rate their mental health
    
Rating_MetalHealth= int(input("Please enter your mental health rating (on a scale of 1-10) : "))
if Rating_MetalHealth >= 7:
    print("That's great! Keep up the positive mindset! an be happy always")
elif Rating_MetalHealth >= 4:
    print("It seems like an average day. Take care of yourself! and avoid bad groups")
else:
    print("I'm sorry to hear that. Reach out for support if needed.")
    
           
    
