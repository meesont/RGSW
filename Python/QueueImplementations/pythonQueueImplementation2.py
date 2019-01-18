from collections import deque

d = deque() #Deque requires popping from the left as functions as a normal list otherwise

for i in range(0, 10):
    d.append(i)


print(d)
print(d.pop()) #Popping normally pops from the right which
print(d.popleft())
print(d)
