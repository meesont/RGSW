#Generators vs comprehension
'''
Generators use much less memory than comprehension however is slower
Generators create the values on the fly (range() is a generator expression)
List comprehension processes the entire list at once and stores it in memory, therefore
functioning quicker however using more memory
'''
import functools, time


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


#This is a generator expression
@timing #timing decorator
def generator():
    xyz = (i for i in range(500000))
    print(list(xyz)[:5])
    

@timing
def comprehension():
    abc = [i for i in range(500000)]
    print(abc[:5])    


if __name__ == '__main__':
    generator()
    comprehension()