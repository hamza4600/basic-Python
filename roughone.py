# program to get the mutlpleof 7 and not divided by 5
l=[]
for i in range (2000, 3200):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))  
        
print("," .join(l))
          
        #   find factorial of numebr from input
def factorial(x):
    if x==0:
        return 1
    return x* factorial(x-1)
x=int(input())
print(factorial(x))

# print out thr range and n+1 dict is an Object empty
n=int(input())
d=dict()
for i in range(1,n+1):
    d[i]=i*i
print(d)

# convert the input to the List and Tuple input should in , 
value=input()
l=value.split(",")
t=tuple(l)
print(l)
print(t)
# simple functions created to get output 
def add(a,b):
    return print(a+b)
add(10,20)  

    
