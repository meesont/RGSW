class Queue: #OOP based queue implementation
    def __init__(self):
        self.items = []
    def enQueue(self, value):
        self.items.insert(0, value)
    def deQueue(self):
        self.items.pop()
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)
    def getQueue(self):
        return self.items

q = Queue() #Instatntiate an instance of the class

print(q.enQueue('Tom'))
print(q.enQueue('Bob'))
print(q.getQueue())
print(q.size())
print(q.deQueue())
print(q.getQueue())
print(q.isEmpty())
