import random as r

arrSize = int(input('Enter size of array to search: '))
searchTerm = int(input('Enter search term for the array: '))
array = []

def createArray(size):
    for i in range(0, arrSize):
        array.append(i)

def linearSearch(arr, value):
    for i in arr:
        if arr[i] == value:
            return i
