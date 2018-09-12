thisFishSize = 1
thisFishState = "fish"

def feed(state, size):
    size += 1
    print("Fish Fed")
    if size == 5:
        state = "FISH"
        
    return size

print(thisFishState + " is size of " + str(thisFishSize))
while thisFishSize != 5:
    thisFishSize = feed(thisFishState, thisFishSize)
print("It is now a big " + thisFishState)