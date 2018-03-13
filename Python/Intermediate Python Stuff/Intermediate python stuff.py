#Intermediate Python stuff
from os import path

names = ["Tom","Jon","Bob","Chris"]

for name in names:
    output = ' '.join(["hello there,", name])
    print (output)
    

filePath = "/Users/thomas/Documents/School Coding - Github/RGSW/Python/Intermediate Python Stuff"
fileName = "default.txt"

#Use .join rather than using +
#.join scales better than + does therefore better for larger projects

with open(path.join(filePath, fileName)) as file:
    print(file.read())
    

name = "Tim"
apples = 10

print(f"Today {name} bought {apples} apples!")
print("Today {} bought {} apples!".format(name, apples))
