from numpy.random import seed
from numpy.random import randint


def linearSearch(arr, value):
    for i in arr:
        if arr[i] == value:
            return i

if __name__ == '__main__':

    seed(1)

    arrSize = int(input('Enter size of array to search: '))
    searchTerm = int(input('Enter search term for the array: '))

    array = randint(0, arrSize, arrSize)
    # print(array)

    print(linearSearch(array, searchTerm))
