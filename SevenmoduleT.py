# use  functions and import then from the One file

import SevenmoduleO as one
import platform
from SevenmoduleO import person1 # only import a single Object
# time Module 
import time
sec=time.time()
print("seconds start from " +str(sec))

# printing the local time ctime take time in seconds in argument
local=time.ctime(sec)
print("Local time is ", local)

# sleep() delay the execution of a function
def delay():
    print("Printing utput after some time")
    time.sleep(2)
    print("After 2 secomds")
    
delay()
    
    # digital clock
def digital():    
    while True:
        localtim =time.localtime()
        rest=time.strftime("%I:%M:%S:%P",localtim)
        print(rest)
        time.sleep(1)
    



x=platform.system()
print("Your system is " + x)


one.greeting("Hamza")

oo=one.person1
print(oo)

# we can also use keyword from as importing a specifi function from a file 

# runningthe clock 
digital()        
