# It is used to view the memory area of the string and nu,ber
x=memoryview(bytes(5))
print(x)    
def mutliple(a,b):
    return print(a*b)
        
y=mutliple(1092,80)
p=memoryview(bytes(9000))
print(p)

# It is array to store collection of binary data in the area
o=bytearray(10)
print(o)

# It return an oBJECT with  given size and data it take three parameter bytes([source[,encoding[,error]]]) if source is a string then we have to encode the string below is byte of given integer size
D=bytes(6)
print(D)
# convert string to Bytes
arr="Hamza Khan"
att=bytes(arr, "utf-8")
print(att)

# Numbers
# complex number
q=3+5j
print(type(q))
# float
fg= -35.485456445
print(type(fg))
# M=Now we will convert them to each other is now an int
sd=int(fg)
print(type(sd))

# each time this will generate a Random Number
import random
print(random.randrange(1,50))

# Casting in Python it has converted it to a float sam eis case in int() flat () and str()
we=float("5")
print(we)       

# type have been converted to String
qs=str(45604564554455)
print(type(qs))

# String and Methods

fg="Hello Lahore In pakistan"
# it will return the first chraters from the array
print(fg[1])
print(fg[3])

# loop  alllthe letters from the array 
for x in fg:
    print(x)
    # lendgth of string

print("Letters in String are" +" "+ str(len(fg)))
    
#  in an If statmentto check if a word is a paragraf or not
print("In" in fg)
if "In" in fg:
    print("Yes Letter is Present in the Pharase")
    # same cose in not in if present

fgs="Pakistan Lahore Jangh London" 
if "pakistan" not in fgs:
    print("Not Present In Tetxt Field")    
    
    # slice the text start fro 0 index copy first 11 charater
ty="Hello world How is Tesla Going On ??"
print(ty[:10])

# slice to the end  from end to start 11 character
print(ty[10:])
# now slice the Text from the an range in -z-index
print(ty[-12:-3])
# Modufy the string
print(ty.upper())
print(ty.lower())
print(ty.strip())

# replace a string with another o with X
print(ty.replace("o" ,"X")) 

# split sub string 
print(ty.split(","))

a = "Hello, World!"
print(a.split(",")) 

# addd in string with a Interger Value
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age)) 
# another example
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# we can also use Index Value
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# Especia Charcter
txt="My Name is \"Hamza Khan\" How is Commas"
print(txt)
# for new Line
tx=t="My Name is \n Hamza Khan\n How is Commas"
print(tx)
# there are many more Build In methods in Pythos for String we will use Later

