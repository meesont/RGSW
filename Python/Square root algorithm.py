number = int(input("Enter a number to find the square root for: "))
n = 0

correct = False
while correct == False:
    nsquared = n*n
    if(nsquared == number):
        print("The integer is: " + str(n))
        correct = True
    else:
        n = n + 1
        #print(str(nsquared))
        correct = False