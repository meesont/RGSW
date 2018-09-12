num1 = int(input("Etner a whole number: "))
num2 = int(input("Enter another whole number: "))

temp1 = num1
temp2 = num2


while temp1 != temp2:
    if temp1 > temp2:
        temp1 = temp1 - temp2
    else:
        temp2 = temp2 - temp1  
        
result = temp1
print(f"{result} is GCF of {num1} and {num2}")