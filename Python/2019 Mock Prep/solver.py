def loadwords(file):
    allowedWords = []
    with open(file + '.txt', 'r') as f:
        for word in f:
            allowedWords.append(word.strip().upper())
    return allowedWords

def GetStartingHand(TileQueue, StartHandSize):
    Hand = ""
    for Count in range(StartHandSize):
        Hand += TileQueue.Remove()
        TileQueue.Add()
    return Hand

# def validateWord(word, allowedWords):


'''
Weight each character with the correct weightings #DONE
Iterate through characters generated and pick the ones with heighest ratings
Formulate a valid word from the highest weighted characters (use a queue to select heighst first)
Check the word is valid

Weightings for characters
{'A': 1, 'B': 2, 'C': 2, 'D': 2, 'E': 1, 'F': 3, 'G': 2, 'H': 3, 'I': 1, 'J': 5, 'K': 3, 'L': 2,
 'M': 2, 'N': 1, 'O': 1, 'P': 2, 'Q': 5, 'R': 1, 'S': 1, 'T': 1, 'U': 2, 'V': 3, 'W': 3, 'X': 5,
 'Y': 3, 'Z': 5}

Will use practice hands to begin with

'''

tileDict = {'A': 1, 'B': 2, 'C': 2, 'D': 2, 'E': 1, 'F': 3, 'G': 2, 'H': 3, 'I': 1, 'J': 5, 'K': 3, 'L': 2,
 'M': 2, 'N': 1, 'O': 1, 'P': 2, 'Q': 5, 'R': 1, 'S': 1, 'T': 1, 'U': 2, 'V': 3, 'W': 3, 'X': 5,
 'Y': 3, 'Z': 5}

startHand = GetStartingHand()


words = loadwords('aqawords')
