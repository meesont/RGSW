#Fractorial function

def fractorial(x):
    y = 0
    total = 0
    while y <= x:
        temp = y
        total += ((y+1) * temp)
    return total

print(fractorial(5))

for(i in range(0,10)):
    print(fractorial(i))
