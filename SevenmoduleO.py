# we will define function in this file and use in Two files
# Date Object 

import datetime
#using multthread for performance and tasks
# we can also use strftime for converting the date and time to string
import threading
# defining a loop in a function using multiple threading power of chip
def mutlithread():
  for i in range(5):
    print("Hamza")
     
def mutlithreadT():
  for i in range(5):
    print("London NSA")
    
t1=threading.Thread(target=mutlithread)     
t2=threading.Thread(target=mutlithreadT)
t1.start()    
t2.start()    


x=datetime.datetime.now()
print("Years Month day hours seconds and Milli " + str(x))

# Only Year and days  using strftime()
print("Years is " + str(x.year))
print(x.strftime("%A")) 
 
#  we can also set Date and time Object and pass it as argumnet 
y=datetime.datetime(2025, 1, 3)
print("Future Time is " + str(y))
 
 
def greeting(name):
    print("Hello " + name)
    
    #Object  
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}      

