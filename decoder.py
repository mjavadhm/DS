def read_huffman_codes(file_path):
    huffman_codes = {}
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            char, code = line.strip().split(':')
            huffman_codes[char] = code
    return huffman_codes

def read_compressed_text(file_path):
    with open(file_path, 'rb') as file:
        compressed_data = file.read()
    return bin(int.from_bytes(compressed_data, byteorder='big'))[2:]


def decode_text(compressed_text, huffman_codes):
    decoded_text = ""
    current_code = ""

    for bit in compressed_text:
        current_code += bit
        for char, code in huffman_codes.items():
            if current_code == code:
                if char == 'ƒ':
                    decoded_text += '\n'
                    current_code = ""
                else:
                    decoded_text += char
                    current_code = ""

    return decoded_text


def write_decoded_text(decoded_text, output_file):
    with open(output_file, 'w') as file:
        file.write(decoded_text)


def main(): 
    huffman_key_file = 'huffman_key.txt'
    huffman_codes = read_huffman_codes(huffman_key_file)
    compressed_text = read_compressed_text('compressed_file.bin')
    decoded_dna = decode_text(compressed_text, huffman_codes)
    write_decoded_text(decoded_dna, 'order.txt')

if __name__ == '__main__':
    main()