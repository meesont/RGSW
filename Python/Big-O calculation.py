# This program counts the number of print statements
# executed for a list of a given size
# This gives a measure of how many  print statements are executed
# The number of times the loops are executed is more significant
#than the number of statements in each loop

def bigO(aList):
     numberOfPrints = 0
     n = len(aList)
     for i in range(0,n):
          print("In outer loop: ",aList[i])
          numberOfPrints = numberOfPrints + 1
          for j in range(int(n/2)):
               print("    In inner loop: ",aList[j])
               numberOfPrints = numberOfPrints + 1
     print("\n")     
     print("number Of Print statements executed: ", numberOfPrints)
     numberOfPrints = numberOfPrints + 1
     print("\nAdd an extra one, so total =: ", numberOfPrints)

listOfItems = [1,2,3,4,5,6]
bigO(listOfItems)
print ("length of list: ", len(listOfItems))