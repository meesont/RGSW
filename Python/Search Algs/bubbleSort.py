import random as r

toSort = []

for i in range(10):
    toSort.append(r.randint(0, 100))

def bubbleSort(list)
    for i in list:
        if list[i] > list[i+1]:
            list[i], list[i+1] = list[i+1], list[i]
