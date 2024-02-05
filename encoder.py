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
        if dna[j] == worker[i]:
            i += 1
            j += 1
            
            if j == len(dna):
                return True
        else:
            if j != 0:
                j = shekast[j-1]
            else:
                i += 1
    
    return False

def fshekast(pat):
    shekast = [0] * len(pat)
    length = 0
    i = 1
    
    while i < len(pat):
        if pat[i] == pat[length]:
            length += 1
            shekast[i] = length
            i += 1
        else:
            if length != 0:
                length = shekast[length-1]
            else:
                shekast[i] = 0
                i += 1
    
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
    count = {}
    for k in range(queue.size()):
        i=0
        dna = queue.dequeue()
        while i < len(queen):
            j=0
            while j < len(worker):
                if isok(dna=dna,queen=queen[i],worker=worker[j]):
                    tqueue.enqueue(dna)
                    for letter in dna:
                        if letter in count:
                            count[letter] += 1
                        else:
                            count[letter] = 1

                    
                    i,j = 200,200
                else:
                    j += 1
            i += 1
    letters = []
    frequent = []
    for letter, frequency in count.items():
        letters.append(letter)
        frequent.append(frequency)
    
    for k in range(len(letters)):
        #dna = tqueue.dequeue()
        print(f"{letters[k]}   -   {frequent[k]}\n-----")
    


main()