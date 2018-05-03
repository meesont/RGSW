#AS Computer Science Specimen

howFar = int(input("How far to count: "))

while howFar < 1:
    howFar = int(input("Not a valid number, please try again: "))
    
for x in range(howFar + 1):
    if((x % 3 == 0) and (x % 5 == 0)):
        print("Fizz Buzz")
    elif (x % 3 == 0):
        print("Fizz")
    elif (x % 5 == 0):
        print("Buzz")
    else:
        print(x)
