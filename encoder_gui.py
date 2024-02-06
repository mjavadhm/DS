import tkinter as tk
from tkinter import filedialog
import subprocess

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

queen = []
worker = []
queue = Queue()
tqueue = Queue()
huffman_codes = {}
files_imported = False
key_generated = False

def create_window():
    color = 'dark blue'
    window = tk.Tk()
    window.geometry("800x500+200+100")
    window.title("Encoder")
    window.configure(background=color)
    
    text_label = tk.Label(window, text="\n\n\nTo get started, import your files using Import Files.\n\n\nThen find the Huffman code for each letter with Generate Huffman Key.\n\n\nFinally, compress and save the file using Encode.\n\n\nOr just use One Click Encode\n\n\nthen use secode to generate order.txt", bg=color, fg="white")
    text_label.pack()

    empty_space = tk.Label(window, text="",bg=color)
    empty_space.pack()

    button_frame = tk.Frame(window,  bg=color)
    button_frame.pack()

    import_button = tk.Button(button_frame, text="Import Files", command=import_files)
    import_button.grid(row=30, column=30, padx=20, pady=20)

    key_button = tk.Button(button_frame, text="Generate Huffman Key", command=generate_huffman_code)
    key_button.grid(row=30, column=31, padx=20, pady=20)

    encode_button = tk.Button(button_frame, text="Encode", command=encode_text)
    encode_button.grid(row=30, column=32, padx=20, pady=20)

    empty_space.pack()

    oencode_button = tk.Button(button_frame, text="One Click Encode", command=oencode_text, bg="yellow", fg="black")
    oencode_button.grid(row=49, column=31, padx=20, pady=20)

    decode_button = tk.Button(button_frame, text="Decode", command=decode_text)
    decode_button.grid(row=50, column=31, padx=20, pady=20)

    window.mainloop()


def decode_text():
    subprocess.call('python decoder.py', shell=True)

def import_files():
    global queen, worker, queue, files_imported
    queen, worker = read_parents()
    read_input()
    files_imported = True

def generate_huffman_code():
    global queen, worker, queue, huffman_codes, tqueue, key_generated, files_imported
    if not files_imported:
        tk.messagebox.showerror("Error", "Please import files before generating Huffman key.")
        return
    else:
        count = {}
        letters = []
        frequent = []
    
        for k in range(queue.size()):
            i = 0
            dna = queue.dequeue()
            while i < len(queen):
                j = 0
                while j < len(worker):
                    if isok(dna=dna, queen=queen[i], worker=worker[j]):
                        print(f'{dna}\n--------')
                        tqueue.enqueue(dna)
                        for letter in dna:
                            if letter in count:
                                count[letter] += 1
                            else:
                                count[letter] = 1
                    
                        i, j = 200, 200
                    else:
                        j += 1
                i += 1
        count['ƒ'] = tqueue.size() - 1
        for letter, frequency in count.items():
            frequent, letters = binsert(frequent=frequent, fre=frequency, letter=letter, letters=letters)
    
        for k in range(len(letters)):
            print('Letter:', letters[k], 'frequent:', frequent[k])
    
        huffman_codes= {}
        huffman_codes = huffman_code(letters, frequent)
        savekey(huffman_codes)
        key_generated = True
        files_imported = False

def encode_text():
    global huffman_codes, tqueue, key_generated
    if key_generated:
        compressed_dna = compress_text()
        write_compressed_text(compressed_dna, 'compressed_file.bin')
        key_generated = False
    else:
        tk.messagebox.showerror("Error", "Please generating Huffman key before Encode.")
        return


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
    
def oencode_text():
    import_files()
    generate_huffman_code()
    encode_text()

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

def read_input():
    global queue
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        
        for line in lines:
            dna = line.strip()
            queue.enqueue(dna)

def binsert(frequent, fre,letter,letters):
    low = 0
    high = len(frequent) - 1

    while low <= high:
        mid = (low + high) // 2
        if frequent[mid] < fre:
            low = mid + 1
        else:
            high = mid - 1

    frequent.insert(low, fre)
    letters.insert(low, letter)
    return frequent ,letters

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x.freq < pivot.freq]
    middle = [x for x in arr if x.freq == pivot.freq]
    right = [x for x in arr if x.freq > pivot.freq]
    return quicksort(left) + middle + quicksort(right)

class Node:
    def __init__(self, freq, letter=None, left=None, right=None):
        self.freq = freq
        self.letter = letter
        self.left = left
        self.right = right

def huffman_code(letters, frequent):
    global huffman_codes, tqueue
    nodes = []
    for i in range(len(letters)):
        node = Node(frequent[i], letters[i])
        nodes.append(node)
    
    while len(nodes) > 1:
        nodes = quicksort(nodes)
        
        left = nodes.pop(0)
        right = nodes.pop(0)
        
        new_freq = left.freq + right.freq
        new_node = Node(new_freq, left=left, right=right)
        nodes.append(new_node)
    
    root = nodes[0]
    codes = {}
    
    def find_codes(node, code):
        if node.letter:
            codes[node.letter] = code
        else:
            find_codes(node.left, code + '0')
            find_codes(node.right, code + '1')
    
    find_codes(root, '')
    
    return codes

def compress_text():
    global huffman_codes, tqueue
    compressed_text = ""
    while not tqueue.is_empty():
        dna = tqueue.dequeue()
        for char in dna:
            compressed_text += huffman_codes[char]
        if tqueue.size() > 1:
            compressed_text += huffman_codes['ƒ']

    return compressed_text

def write_compressed_text(compressed_text, output_file):
    with open(output_file, 'wb') as file:
        file.write(int(compressed_text, 2).to_bytes((len(compressed_text) + 7) // 8, byteorder='big'))

def savekey(huffman_codes):
    with open('huffman_key.txt', 'w') as file:
        for char, code in huffman_codes.items():
            file.write(f"{char}:{code}\n")

if __name__ == '__main__':
    create_window()
