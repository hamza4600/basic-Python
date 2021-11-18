
# Boolen  in Pyhton 
a=500
b=350
if b>a:
    print("b ir greater than a")
else:
    print("a is greater than b")
    
    # bool() function allow values and return true or flase Most values are true
    # some values are false if no data is in avarible or in anm array Object Tuple 
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({})) 

# we can also return boolen from a function
def myFunction() :
  return True

print(myFunction()) 
# we can also execute a cosde on the bases or Boolen 

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")    

            # is an example of list type of aray in Python
list1 = ["abc", 34, True, 40, "male"]     

# floor division ron of to nearest number 
x = 15
y = 2

print(x // y)

# Modules show reminder assign operators are as s+=10 means s=s+10 
d=5
d%=3
print(d)

# comparison operators return false
f=29
q=49
print(f==q)

#mostaly used for Objetcs  membership operator return true an false
po=["apple","Lahahz"]
print("apple" in po)
# same exaple for  not in 
print("Lahore" not in po)
              
              