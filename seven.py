# python also have build in math Object that have large number Build in modules  we an use 
import math
# json  for Json Notation
import json
a=math.pi
print("Vale of PI is " + str(a))

# max() and  min()  for gerting the minimal and maximam number
x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

# abs() return positive value of a specific value 
g=abs(-560145.44454)
print(g)
 
#  pow() take two argumant and return as power 
d=pow(5,5)
print(d)

# sqrt() return sqiure root of that number
qa=math.sqrt(25100)
print(qa)

# math.ceil()  roun off number to upper case 
po=math.ceil(53.236)
print(po)
# math.floor() round of number to lower case 
pa=math.floor(55.8956)
print(pa)

# Json In Python
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
yy=json.loads(x)
print(yy["age"])
print(x)

# we will convert Python Object to Json dumps()
a = json.dumps(x)
print(a)

# by using json.dump() we can convert all the data types in json Object
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))


# in above eample we have simple Output for intendationwe have parametr in json.dump(x, indent=4) indent define the intendation and x is Object

xa = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
} 
print("JavaScript OBject ")
print(json.dumps(xa, indent=4))

# try except finally patttern in Python for running and Handelling the  code
def tryexcept():
    try:
        print(za)
    except NameError:
        print("VArible Name is not define")
    except:
        print("General error")
                    
tryexcept()        

# finally in example
def finaltry():
    try:
        print(sa)
    except:
        print("Something went wrong")
    finally:
        print("The try has been finished")        
    
finaltry()

#fake python program that will open and read file
def fileread():
    try:
        f=open("demo.txt")
        try:
            f.write("random tetx to the file")
        except:
            print("Something went wrong")
        finally:
            f.close()
    except:
        print("Something went wrong in reading file")
        
fileread()
            
                    #  formate() fordynamic data ina string or a field like Data # base 
                      
da=234
txt="Random Txt {} in the Dollars"
print(txt.format(da))
                    #   we can also use index value of a varible as we want or defie
def IndeT():
    quantity = 3
    itemno = 567
    price = 49
    myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."                    
    print(myorder.format(quantity,itemno,price))
    
IndeT()
    #another example
def AnotherI():
    age = 24
    name = "Hamza"
    txt = "His name is {1}. {1} is {0} years old."
    print(txt.format(age, name))
    
AnotherI()
# Naming convention method can also be used 
def NamE():
    myorder = "I have a {one}, it is a {two}."
    print(myorder.format(one = "Ford", two = "Mustang"))

NamE()
     
    #  basic example of re for serch pattern in a tetx of a file 
    