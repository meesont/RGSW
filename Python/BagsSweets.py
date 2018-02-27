#Bags/Sweets program
bags = int(input("Enter the number of bags you have: "))
sweets = int(input("Enter the number of sweets you have (must be greater than that of the number of bags): "))

while bags >= sweets:
    sweets = int(input((f"Please enter a number of sweets larger than {bags}: ")))
    
if(sweets/bags) % 2 == 0:
    print("It is possible to put an odd number of sweets in each bag")
else:
    print("It is not possible to put an odd number of sweets in each bag.")
    