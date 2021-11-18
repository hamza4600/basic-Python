# discussing List indetails
# list Item are Index we can acces they by index value 
list=["aple","orange","kite"]
print(list[2] )

# Range in search can be specify by the index value we enter  below start from 2 an d end at 5   indedx
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) 

# Leaving the item from an array all remaing will be printed  last will be remove from array
thislists = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislists[:6])
# by enter like this it will star from the index we enter first two are remove 
print(thislists[2:])
# we can also specift negaitive range froma list -1 last item will be not in the array
print(thislists[-4:-1])
# check if an item exist in an item
if "apple" in thislists:
    print("Value is present in the list")
    
    #now we wil change value from a List  
thislistq = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislistq[1:3]=["Lahore", "London"]
print(thislistq)
    # change a range of vales from a list 2 and 3 value are replace by single value print only two values 

thislis = ["apple", "banana", "cherry"]
thislis[1:3] = ["watermelon"]
print(thislis)     

# using Insert () function we can  inseert new value without replacing a value  print four values 
thisLis=['Hamza','Hasssan','Sameer']
thisLis.insert(2,"Paksitan")
print(thisLis)

# we can add a list to end a new List by useing append() function 
aa=['One','Two','Three']
bb=["Foure","five", "Six"]
aa.append(bb)
print(aa)

#using insert() to insert a value in a specify Index Value 
ab=['One','Two','Three']
ab.insert(3,"Hundered")
print(ab)

# Extend a List using extend() Method  add item at last
aa=['One','Two','Three']
bb=["Foure","five", "Six"]
aa.extend(bb)
print(aa)

# remove() Removing Items from a List remove selected item
ad=['One','Two','Three']
ad.remove("Three")
print(ad)

# pop() remove item from Indexx value and if we don,t specify it remove item fom LAst
ada=['One','Two','Three']
ada.pop(2)
print(ada)

# del  is also used to remove item according to index value
ae=['One','Two','Three']
del ae[0]
print(ae)

# clear is used to remove all list an become emplty


# loop all usin For item from a list
af=['One','Two','Three']
for x in af:
    print(x)
    # same exapmle using while loop
i=0
while i<len(af):
    print(af[i])
    i=i+1 
       
    #    loop through index number using range() and  len() function
lop=["Lion","King", "Karachi"]
for i in range(len(lop)):
    print(lop[i])
    
    
# we can creat a new list onnbases of  previus list and add elemnet according conditional statemt if true
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)
# print words with having a ina new list
print(newlist) 

# we can also do inverse item that are presenvet skip it and print the list
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newfruit=[x for x in fruits if x !="apple"]
# skippes teh apple in the new list
print(newfruit)

# Print a range with  a List 
newNumber=[q for q in range(20)]
print(newNumber)
# below code will print only greater to 5 
neNumber=[a for a in range(10) if a>5]
print(neNumber)

# now conver small letter in Uppper case in an range of list
neFruit=[h.upper() for h in fruits]
print(neFruit)

# now we will set a single varible to al list 
nezz=["Hamza" for w in fruits]
print(nezz)

# now we will sort the list accorging to Alpgabetically and Numerically
fruitlist = ["orange", "mango", "kiwi", "pineapple", "banana"]
fruitlist.sort()
# arrange in alpbetically order
print(fruitlist)

numberlist = [100, 50, 65, 82, 23]
numberlist.sort()
print(numberlist)

# we can also reverse the item using reverse function in a List items if we set to true then it will 100,99 patern 
fruitlist.reverse()
print(fruitlist)
# if we have capital letters in a list Capotal will be placed first

# customize a function and aply Logic on it
def funcReverse(n):
   return abs(n-1)

example=[100, 50, 65, 82, 23]
example.sort(key=funcReverse)
# arrange  the numberically and from 50 to 100
print(example) 
        
        # copy the item from a list using Build in functions
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)        

# 2 nd metyhod
thislist = ["apple", "banana", "cherry"]
mylist10 = list(thislist)
print(mylist10)

# Joining two list with each other 3 methods
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3) 
# 2 nd metyhod

list1 = ["a", "b" , "Hamza"]
list2 = [1, 2, 3, 4 ]

for x in list2:
  list1.append(x)
# add item to ist list and render 
print(list1) 

# using exted method add list of fruit in a list
list1.extend(fruits)
print(list1)
    
    
        
    


