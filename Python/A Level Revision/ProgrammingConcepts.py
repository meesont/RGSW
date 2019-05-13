import Constants as consts
# Primative data types
char = 'a'
int = 1
float = 1.1
boolean = True
string = "hello world"
oneDimensionalArray = [i for i in range(10)] # comprehension expression to fill array with 50 items
# twoDimensionalArray = [1, 2][3, 4]

print(consts.PI) #Const declaration

# iteration through an array
for i in range(len(oneDimensionalArray)):
    print(oneDimensionalArray[i])

# nested selection
chars = ['d', 'c', 'b', 'a']
if('a' in chars):
    if('a' != 'b'):
        print('YES!')
        print('')
        print('')
    elif ('a' == 'a'):
        print('Route 2')

# exception handling
x = 7
if x < 5:
    raise Exception(f'x should not be < than 5. Value of x was {x}') # this creates an exception and stops program
else:
    try:
        with open('file.txt', r) as f:
            data = f.read()
    except:
        print('could not open file.txt')
        pass

# function definition with parameters/default parameters
def say_hello(name='Tom'):
    print(f'Hello {name}')

say_hello()
