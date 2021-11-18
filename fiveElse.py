# if else statement and conditional statemt for running code
# they are used for conditional statement and  furteher code to run 
a=50
b=100
if b>a:
    print("b is greate than a" )
elif a==b:
    print("a is equal to b")
    # using elif 
else:
    print("a is greate than b")    
    
    # Intendation is important
    
# elfi is used if previous statemnet is wrong  and Else catch  anything which isn,t catch by process  
s = 200
p = 33
if s > p:
  print("s is greater than p")
else:
  print("p is not greater than s")    

    # if we have a single line statemt then it will work as 
if a >  b: print("a is greater than B")    
# and if we have two statemt if and else in a single Line it will be
print("A") if a > b else print("B")
# we can also write thre line OPtion in a single line]
z = 330
x = 330
print("x") if z > x else print("=") if z == x else print("z") 

# now we will discus Logical Operators 
c=50
if a>b and c >a:
    print("Both Conditions are true")
    
if a>b and c >a:
    print("One  condition is true")
    
    # we can also pass as nested statement
    # if statment can not be empty fi emty will show a error
    
    
    # Basic exapmle of while LOop Number up to 10
i=1
while i<11:
    print(i)
    i+=1
    
    # Break is used to stop a Loop 
p=10
while p<20:
    print(p)
    if p==15:
       break
    p+= 1    
    
    # For loop isused for Itteration froma string and Array
for d in "bxshbxdwskckjdnihcascdhbcdl":
    print(d)
        
# arrays
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
        
        # coninue stop iteration a loop  and coninue to next skip the banan and tehn nest but in break it stop the loop  
for q in fruits:
    if q =="banana":
        continue
    print(q)        
    
    #alwys have two numbers we can also use Rang() to print to print a sequience of number we want
for a in range(5,11):
    print(a)
        # if we add three number then sequience will be  after that number incremantal
for d in range(10,55,5):
    print(d)
            
            # else can also be used in Loop wil not break the code 
for x in range(6):
  print(x)
else:
  print("Finally finished!")             
        
        # using it in a range function and if else and break and continue
for x in range(6):
  if x == 3: break #coninue also work as same
  print(x)
else:
  print("Finally finished!")         
        
        # inner Loop 
        
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)         
    
    # for loop can not be emty if emty cause error or enter pass to stop a errorfor 
for x in [0, 1, 2]:
  pass


