import random as r

positionsArr = [None for i in range(3)]
pin = input('Enter the pin: ')

for i in range(3):
    positionsArr[i] = r.randint(0, len(pin))

print(positionsArr)

# TODO: check length of pin
# TODO: check positionsArr 
