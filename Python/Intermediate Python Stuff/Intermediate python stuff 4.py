#Comprehension and generators 2

for i in range(5):
    for ii in range(3):
        print(i, ii)

#These do the same thing (embedded generators)
[[print(i, ii) for ii in range(3)] for i in range(5)]