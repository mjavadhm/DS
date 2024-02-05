class Queue:
    def __init__(self):
        self.ants = []
 
    def is_empty(self):
        return self.ants == []
 
    def enqueue(self, data):
        self.ants.append(data)
 
    def dequeue(self):
        return self.ants.pop(0)
    def size(self):
        return len(self.ants)

def isok(dna,queen,worker):
    if dna[0]==queen[0]:
        if len(dna) == 1:
            return True
        else:
            cdna = dna[1:]
        
            if kmp(dna=cdna,worker=worker):
                return True        
            else:
                return False
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
            if pat[k] == pat[j]

    
    return shekast
def read_parents():
    queen = []
    worker = []
    
    with open('parents.txt', 'r') as file:
        lines = file.readlines()
        
        queens = int(lines[0].strip().split()[0])
        workers = len(lines) - 1 - queens
        
        for i in range(1, queens + 1):
            queen.append(lines[i].strip())
        
        for i in range(queens + 1, queens + workers + 1):
            worker.append(lines[i].strip())

    return queen, worker

def read_input(queue):
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        
        for line in lines:
            dna = line.strip()
            queue.enqueue(dna)

def main():
    queen, worker = read_parents()
    queue = Queue()
    read_input(queue)
    tqueue = Queue()

main()