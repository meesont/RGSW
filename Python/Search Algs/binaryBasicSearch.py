#!/usr/bin/env python3

def binarySearch(list, term):
    lower = 0
    upper = len(list)
    while lower < upper:
        i = lower + (upper - lower) // 2
        val = list[i]
        if term == val:
            return i
        elif term > val:
            if lower == i:
                break
            lower = i
        elif term < val:
            upper = i

def binary_search(array, target):
    lower = 0
    upper = len(array)
    while lower < upper:   # use < instead of <=
        x = lower + (upper - lower) // 2
        val = array[x]
        if target == val:
            return x
        elif target > val:
            if lower == x:   # these two are the actual lines
                break        # you're looking for
            lower = x
        elif target < val:
            upper = x

print(binary_search([1, 2, 5, 15, 34, 54, 89], 89))
