class Queue:
    def __init__(self):
        self.ants = []
 
    def is_empty(self):
        return self.ants == []
 
    def enqueue(self, data):
        self.ants.append(data)
 
    def dequeue(self):
        return self.ants.pop(0)
