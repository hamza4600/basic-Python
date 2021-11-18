
# Object examples
# Objects
class MyClass:
    student=200
p1=MyClass()
print(p1.student)
    
    #init( main fucntion ) for creatingthe templeat fo the Object
    # self paterna is used for refer to cuurent class and is use t access varibles belong to that class
class Person:
    def __init__(self,name, age ,Job):
        self.name=name
        self.age=age
        self.job=Job
        
p1=Person("Ali",29 ,"Labour")
print(p1.name)
print(p1.job)

# init() is used for creating the Objects define a method to a Object
class Student:
    def __init__(self,school,city):
        self.school=school
        self.city=city
        # intendaton can cause error
    def myfun(self):
          print("Hello my name is " + self.school)

p11=Student("Hazar Public","Kashmire")
p11.myfun()

# <modify> the properties of a Object 
p11.city="Multan"
print(p11.city)

# del the proprties of Object if we type del and Object name it wil delete the Object 
del p11.city
            
            # class cannot be emty but if needed pass is used 

#Python Inhereiance allow us to define a class that inherit methods and Properties of other class
# Parent Class Inhertform or Base class
# childern Class from another  alsa as derived

class Persons:
    def __init__(self,fname,ftype):
         self.name=fname
         self.type=ftype
         
    def printName(self):
        print(self.name, self.type)

x2=Persons("Kinza" , "Girls")
x2.printName()             
 
        # creating a class as a Childern 
class Student(Persons):
    pass
# initize and pass data to it
x=Student("Slaman","male")
print(x.name)
x.printName()
# require Otput

    # if we use init() in a childern class it wil cause error and over with prorpeties of Parents  
# But we can define the Parent we want to we want 
class Stuu(Persons):
    def __init__(self, fname, ftype):
        Persons.__init__(self ,fname, ftype)  #can also use super insted of parent
xx=Stuu("Asiya","Female")
xx.printName()        

# we can also use super() we don,t have to define the name of parent it automatically inherit infront of super don,t use self 
    #we can also  adding new propsrtie toa Object from a Parent we have 
class Stxx(Persons):
    def __init__(self, fname, ftype):
        super().__init__(fname, ftype)      
        self.study="MBBS"
        
    def welcom(self):
        print("welcom" , self.name , self.type) 
        
Haa=Stxx("Huma","Female")
print(Haa.study)        
# similarly we can also define the the mehod to it we wnat 
Haa.welcom()


# we use iter() to get the values from a Objexct and next() method also allows us to do so
# to iterate properties from a Object  use STopIteration to stop if for on forever
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)
