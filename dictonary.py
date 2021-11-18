# Dictionary  writen in form of key value pair and 
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

# it don,t allow duplications if have it will skip it 
thisdicta =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdicta) 

# for length of dictionary
print(len(thisdicta))

# we can store any data type in it  BOOlen Number String 
Onedict =	{
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
} 
# we cann access a value  by using braket notation[] and key name in it 
gd=Onedict["colors"]
print(gd)
# get() is a method that work in same way work for value 
# for  geeting the Keys we have keys()
sd=Onedict.keys()
print(sd)
# values() return values of Dicatonary
print(Onedict.values())

# for updating the value in a Dictonary 
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change
car["year"] = 2020
print(x) #after the change

# to itterate all key and Value use item()
print(car.items())

# add new key and value in a Dictonary
car["colors"]="Vanta Black "
print(car)

# to check a item is present in a dict
if "colors" in car:
    print("Colors are present in a Dictonary")

# update() to Update value in a dictonary
car.update({"years":"2025"})
# print updated value 
print(car)

# pop() is used to remove item from a Dict by giving a key
car.pop("model")
print(car)

# popitem() remove last item froma dict  and  del() and key remove the value froma dict  and  clear empty the dict 

# iterate value from a dict using loop and values() and keys() items()
for a in car: 
    print(a)
    
    # print all of them
for a, b in car.items(): 
    print(a, b)    


# we can copy all items froma dict 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)


    # we can also deeep Nested a Dict 
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
} 

    #it can also be done as for making lifed easy 
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)
     
# set value to  sa default varible
jj=car.setdefault("brand")
print(jj)










