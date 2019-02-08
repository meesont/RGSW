from numpy.random import seed
from numpy.random import randint

def binarySearchRecursive(list, term):
    low = 0
    high = len(list)-1

    if(high == 0):
        return (f'{term} was not found in list')
    else:
        mid = (low + high) // 2
        if (term == list[mid]):
            return(f'{term} was found in array')
        else:
            if(list[mid] < term):
                return binarySearchRecursive(list[mid+1:], term)
            else:
                return binarySearchRecursive(list[:mid], term)

def binarySearchIterative(list, term):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) //2

        if(list[mid] == term):
            return (f'{term} found at position {mid}')
        elif (list[mid] > term):
            high = mid-1
        elif (list[mid] < term):
            low = mid+1
        else:
            return (f'{term} not found in list')

if __name__ == "__main__":
    seed(1)

    arrSize = int(input('Enter size of array to search: '))
    searchTerm = int(input('Enter search term for array: '))

    array = randint(0, arrSize, arrSize)
    print(array)

    # print(binarySearchRecursive(array, searchTerm))
    print(binarySearchIterative(array, searchTerm))
