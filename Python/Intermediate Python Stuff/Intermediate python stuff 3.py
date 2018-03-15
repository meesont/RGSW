#Generators vs comprehension
'''
Generators use much less memory than comprehension however is slower
Generators create the values on the fly (range() is a generator expression)
List comprehension processes the entire list at once and stores it in memory, therefore
functioning quicker however using more memory
'''

#This is a generator expression
xyz = (i for i in range(5000))
print(list(xyz)[:5])


abc = [i for i in range(5000)]
print(abc[:5])