class circleQueue():

    #Constructor
    def __init__(self):
        self.size = 0
        self.queue = [None for i in range(size)]
        self.front = self.rear = -1
    def enQueue(self, item):
        if (self.rear + 1) % self.size == self.front:
            return 'Queue is full!'
        #Occurs if queue is empty
        elif self.front == -1:
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = item
        #When queue has items in it but is not full
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = item
    def deQueue(self):
        if(self.front == -1):
            return 'Queue is empty!'
        elif (self.front == self.rear):
            t = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return t
        else:
            t = self.queue[self.front]
            self.front = (self.front+1) % self.size
            return t

    def display(self):
        
