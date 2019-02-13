def loadwords(file):
    allowedWords = []
    with open(file + '.txt', r) as f:
        for word in f:
            allowedWords.append(word.strip().upper())
    return allowedWords

words = loadwords('aqawords')
