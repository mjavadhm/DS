class Queue:
    def __init__(self):
        self.ants = []
 
    def is_empty(self):
        return self.ants == []
 
    def enqueue(self, data):
        self.ants.append(data)
 
    def dequeue(self):
        return self.ants.pop(0)

def isok(dna,queen,worker):
    if dna[0]==queen[0]:
        if kmp(dna=dna,worker=worker):
            return True
    else:
        return False
def kmp(dna, worker):
    shekast = fshekast(dna)
    i = 0
    j = 0
    
    while i < len(worker):
        return

def fshekast(pat):
    shekast = [-1] * len(pat)
    #k = 0
    j = 0

    while j < len(pat):
        k = 0
        while k < j:
            if pat[k] == 

    
    return shekast

