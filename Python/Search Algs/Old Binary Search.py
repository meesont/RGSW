#Binary search algorithm
'''
Recursive will just find if the array contains the value or not.
Iterative will return the values position in the array also
'''
import functools
import time

#Timing decorator (online code)
def timing(func):
    @functools.wraps(func)
    def newfunc(*args, **kwargs):
        startTime = time.time()
        func(*args, **kwargs)
        elapsedTime = time.time() - startTime
        print('[{}] finished in {} ms'.format(
            func.__name__, int(elapsedTime * 1000)))
    return newfunc


@timing
def binarySearchIterative(a_list, val):
    low = 0
    high = len(a_list) - 1
    while low <= high:
        mid = (low + high) // 2
        
        if(a_list[mid] == val):
            return f"{val} found at position {mid}"
        elif (a_list[mid] > val):
            high = mid - 1
        elif (a_list[mid] < val):
            low = mid + 1
        else:
            return f"{val} not found in the list"
           

@timing
def binarySearchRecursive(a_list, val):
    
    low = 0
    high = len(a_list) - 1
    
    if high == 0:
        return f'{val} was not found in the list'
    
    else:
        mid = (low + high) // 2 
        if (val == a_list[mid]):
            return f'{val} was found in the array'
        else:
            if(a_list[mid] < val):
                return binarySearchRecursive(a_list[mid+1:], val) #[mid+1:] goes from the value of mid+1 to the end of the list
            else:
                return binarySearchRecursive(a_list[:mid], val) #[:mid] goes from the start of the list to the value of mid     

        
if __name__ == "__main__":
    
    array = []
    arraySize = int(input("enter size of array: "))
    for x in range(0, arraySize):
        array.append(x)
    searchValue = int(input("Enter the value to search for in the array: "))
    
    
    print(binarySearchIterative(array, searchValue))
    print(binarySearchRecursive(array, searchValue))
    