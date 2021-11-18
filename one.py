print("Hello Hamza Khan"); 

if 5>2:
    print("Five is greater than two")
    # declearing simple varaible andf function

x="5"
y="Hello Pakistan"
print(x+y)

# number and Data types
a=str(3)
b=int(3)
c=float(3)
print(type(a))
print(type(b))
print(type(c))

# multiple varible decler in a single line 

d,e,f="Orange","Bnana", "Mango"
print(d,e,f)
# declea  single value varible to multiple varibles 
g=h="Lahore"

# Unpack values from collection
fruit=["One","Two","three "]
i,j,k=fruit
print(i,j,k)
# we can add String by using + but if initeger shows an error

# functions and golbal and Local Varibles in scope
# if we defina Global keyword in side a function then we can use its value Outside of  a functions
l="Awsome Exapmles"
def myfunction():
    l="Fantstic Example"
    global i
    i="Global Varible Value is Outside of Function"
    print("Python is " +l)
myfunction()
print("Pyhton is " +l)
print("Pyhton is " +i)


    