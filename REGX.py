# a regular expression for the search patterns
# buil in module have alot of functions
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt) 
if x:
    print("we have found the result")
else:
    print("Rearch not found")    


# finad all
s= re.findall("in", txt)
print(s)
# search
q=re.search("Lahore", txt)
print(q)
# split all charater ina white spacing
s=re.split("\s", txt)
print(s)

