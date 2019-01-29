toMod = [28, 15, 47, 70, 33, 27, 55, 81, 66, 9, 38]
modVal = 11

for i in range(len(toMod)):
    temp = toMod[i] % modVal
    print(str(toMod[i]) + ' % ' + str(modVal) + ' = ' + str(temp))
