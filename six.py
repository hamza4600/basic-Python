# functions PASS argumneta and call then 
def hello():
    return print("Hello")
hello()
# Now we wil pass argument in this
def hellO(Name):
    print(Name)
hellO("karachi")    
    
    # Number of Argumnets Pass in a function should be same as we define if we pass One or Thee argumnets this will show error
def Two(One,Two):
    print(One +" "+ str(Two).upper())
Two("pakistan","Londeon")        

# If we don,t know how much arrgumnet will be enter in a function we wil have to type * it convert it to a  Tuple and we can performm operations on that
def Large(*kind):
    print("Values Are as"+ " " +(kind[-1]))
Large("hello Paksistan")  

# Print all value froma argumnet using loop
def All(*all):
    for a in all:
        print("Valueas Are Printed "+" "+a)
All("Hamza hammas Ammer" )           

# we can also use double recurrison it we don,t know how much argumnet wil be passed
# def AstDouble(**top):
#     print("last Value from argumnet are" + top)
# AstDouble("Pakistan")    

# setting a default vale to function
def Defalt(koi, msg="Hello Wold"):
    print(koi +" " +msg)
Defalt("Khan")    
    
    # If no argumnet is pass print default values
def Defaultx(country="America"):
    print("i am from "+ country)
Defaultx()        
Defaultx("Pakistan")    

# what ever Data type we pass ina function it will be same as it reach in a function
def Reutn(fox):
    for a in fox:
        print("value are " +a)
fruits = ["apple", "banana", "cherry"]
Reutn(fruits)

# Returna value froma function
def add(a,b):
    return print(a+b)
add(50,10)

        # function defination can,t be empty if empty type pass word to not  occur eror

        #Recurrison in Pyhton 
# function call itsef inside it and return a value to user condition  
 
# factorial of Recursion(10)
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(3)
     
    #  factorial fo recursion
def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


num = 30
print("The factorial of", num, "is", factorial(num))    
         
         
# Lambad afunction annomious functions``
x = lambda a,b: a*b
print(x(10,10))

# add
a= lambda a,b,c: a+b+c
print(a(10,10,10))

# thay are powerful we can use then inside another functions  we can use then anonymous function require
def Main(x):
    return lambda a:a*x
double=Main(2)
triple=Main(3)
print(double(5))
print(triple(5))

# print even number fromlist
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list=list(filter(lambda x: (x%2==0),my_list))
print(new_list)
# similar double a number in list 
new_Double=list(map(lambda a: a*2 ,my_list))
print(new_Double)
         