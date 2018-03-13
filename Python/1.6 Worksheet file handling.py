def displayMenu():
    print("1.  Input data and save to new file")
    print("2.  Input data and append to existing file")
    print("3.  Calculate and display average mark")
    print("4.  Display data")
    print("5.  Quit program")
    choice = input("Enter your choice: ")
    validChoices = ["1", "2", "3", "4", "5"]
    while choice not in validChoices:
        choice = input("Invalid choice! Choose another option: ")
    return choice

def saveToFile(openMode='a'):
    
    studentMark = 0
    studentName = input("Enter a student name, xxx to finish: ")
    while (studentName != "xxx"):
        studentMark = int(input(f"Enter {studentName}'s mark"))
        with open('studentsNamesFile.txt', openMode) as file:
            file.write(studentName + "," + str(studentMark))
        studentName = input("Enter a student name, xxx to finish: ")

def calculateAverage():
    