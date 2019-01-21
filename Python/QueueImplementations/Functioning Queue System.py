import sys

class Queue:
    def __init__(self):
        self.que = []
    def enQueue(self, item):
        self.que.insert(0, item)
    def deQueue(self):
        self.que.pop()
    def isEmpty(self):
        return self.que == []
    def size(self):
        return len(self.que)
    def getQueue(self):
        return self.que

q = Queue() #Instantiate new Queue
usingQueue = True

while usingQueue == True:
    entry = input('Enter new queue value: ')
    q.enQueue(entry)
    cont = input('Continue using queue? (y/n): ')
    if cont == "y":
        usingQueue = True
    else:
        usingQueue = False
