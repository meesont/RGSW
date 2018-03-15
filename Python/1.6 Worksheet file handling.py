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
            file.write(str(studentName) + "," + str(studentMark))
        studentName = input("Enter a student name, xxx to finish: ")

def calculateAverage():
    studentMark = 0
    studentName = ""
    currentLine = ""
    total = 0
    numRecs = 0
    with open('studentsNamesFile.txt', r) as f:
        for line in f.readLine():
            studentName, studentMark = line.split(",")
            numRecs += 1
        total = total + studentMark
    
            