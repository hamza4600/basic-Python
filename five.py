# Tuples in a Pyhthon order unchangeable  and allows duplications
# they allow duplicATE  if items

# determine lenght by using len() fucntion


tuplez=("Hamza","Jamal","Kamal")
print(len(tuplez))

# we have  to  palce a comma in after a single tuple other wise pyhton call it strign``
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# they can be any data Numbef string and Boolean
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

# or Different Data tpes mix of all
# we an also creat a tuple with doble Brackets a use double Brackets
qas = tuple((1,2,3,4,5))
print(qas)

# we can access tuple item as we call a array from a Index value 
tupleOne= ("apple", "banana", "cherry")
print(tupleOne[0])

# negative Neviagtion call item from left side and call from a range as in List
print(tupleOne[-1])
# from a range
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
# leave two item from left side from a tupel
print(thistuple[2:])
#  it will leave item from right side two items
print(thistuple[:2])
# similar we can also apply a range from a list  print one item 
print(thistuple[-2:-1])

# to check if item is prisent in a aray
if "apple" in thistuple:
    print("Apple is present in tuple")
    
    # we can not add a item in a  tupel they are uncahngeable but we can manuplate it by convetring it in a list then back to a tuple 
gag=("One","Two","Three")
aga=list(gag)
aga[0]="Karachi"
gag=tuple(aga)
print(gag)

# simailra we cannot append them so we have to convert them in a list then follw the Above Process

# But we can adda Tuple in a Tuple
One=(1,2,3,4,5)
two=(6,7,8,9)
One +=two
print(One)
# we cannot remove a item from atuple but if we convert back to list then we can

# unpack a Tuple wwe can use it Like a Array method in JS
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

# If varible assign are not equal to atuple then we have to use asstress *
ruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = ruits

print(green)
print(yellow)
print(red)
# if we assign a * a varible in a middle then we have to use , otherwise It will work like as a Varibale
qruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = qruits

print(green)
print(tropic)
print(red) 


# looping throw a Tuple
for g in qruits:
    print(g)
    # also use a while loop
    
    # looping throw a Index Vale and using Build in range() and Len()
for x in range(len(qruits)):
    print(qruits[x])
        
        # find item froma Name return Index value
ha=qruits.index("cherry")
print(ha)
        
# Pyhton SET type of Array
myset = {"apple", "banana", "cherry"} 
print(myset)

# they are used to store Multiple value to a single varible  it is Unorder ,unChangable and UnMixable
# they don,t allow dupliaction  if we have a dupliacte item it will be ignore
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset) 

# determine lenth by using len() fucntion can can s et all type of item in a set  Number string Boolen
# ?we can creat a set by using set() with double brackets
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset) 

# iterrate item from sa set Usig for Loop
for a in thisset:
    print(a)
    
# to check a item is present in a set return boolen value
print("apple" in thisset)

# we a item a set use add()  addin two sets 
setOne={"One","Two","Three"}
setWo={"Five","Six"}
setOne.update(setWo)
print(setOne)
# add()
setOne.add("Thousand")
print(setOne)

# update() to update set we can add list tuple and Dictionary
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset) 

# remove a items from a set and also to del and empty
thisset.remove("apple")
print(thisset)
# similar for discard  and pop() pop remove last item  clear() and del() are used to empty and del set 

# for loop is used to iterate item from a  set 

# there  are  several ways to join or add a set with each other
# union method return a new set withh aded two sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3) 

# similar for update   these both will exicute the duplicate item 
# to only keep a dplaicet item x = {"apple", "banana", "cherry"}
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)
print(x) 

# and intersection will return items that are present in the set  same method
                
     


