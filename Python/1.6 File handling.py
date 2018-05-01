#1.6 File handling program
from sys import exit

#Quality of life methods

def getLines(file):
    lines = 0
    with open(file, 'r') as f:
        for line in f:
            lines += 1
    return lines


#Main Methods

def displayMenu():
    valid = False
    print("1. Input data and save to new file")
    print("2. Input data and append to existing file")
    print("3. Calculate and display average mark")
    print("4. Display data")
    print("5. Quit")
    choice = str(input("Enter your choice: "))
    
    validChoices = ["1", "2", "3", "4", "5"]
    while choice not in validChoices:
        choice = input("Invalid choice! Choose another option: ")    
    return choice
        
def saveToFile(mode):
    with open("testResultsFile.txt", mode) as f:
        studentMark = "0"
        studentName = input("Enter a student name, enter 'xxx' to finish: ")
        while (studentName != "xxx"):
            
            studentMark = str(input("Enter mark: "))
            studentRecord = studentName + ':' + studentMark
            f.write(studentRecord + "\n")
            studentName = input("Enter a student name, enter 'xxx' to finish: ")

            
def calculateAverage():
    total = 0
    records = 0
    avg = 0
    with open ("testResultsFile.txt", 'r') as f:
        for i in range(getLines("testResultsFile.txt")):
            studentRecord = f.readline().split(':')
            studentMark = studentRecord[1]
            total += int(studentMark)
            records += 1
    avg = total / records
    return avg

def displayData():
    with open("testResultsFile.txt", 'r') as f:
        for i in range(getLines("testResultsFile.txt")):
            studentRecord = f.readline().split(':')
            print("Name: " + studentRecord[0] + "\nMark: " + studentRecord[1])
            
            
#Main program
option = displayMenu()

if (option == "1"):
    saveToFile('w')
elif (option == "2"):
    saveToFile('a')
elif (option == "3"):
    print(calculateAverage())
elif (option == "4"):
    displayData()
elif (option == "5"):
    sys.exit()
else:
    option = displayMenu()

print("You chose to quit!")
