#
# Kellen McBurnett
# Apr 27 2025
# File Encryption and Decryption Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

encry_library = {'A': '!', 'B': '@', 'C': '#', 'D': '$', 'E': '%', 'F': '^', 'G': '&', 'H': '*', 'I': '(', 
                 'J': ')', 'K': '-', 'L': '_', 'M': '+', 'N': '=', 'O': '{', 'P': '}', 'Q': '[', 'R': ']', 
                 'S': '|', 'T': ';', 'U': ':', 'V': ',', 'W': '<', 'X': '/', 'Y': '>', 'Z': '?', 'a': '1', 
                 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '0', 
                 'k': 'a', 'l': 'b', 'm': 'c', 'n': 'd', 'o': 'e', 'p': 'f', 'q': 'g', 'r': 'h', 's': 'i', 
                 't': 'j', 'u': 'k', 'v': 'l', 'w': 'm', 'x': 'n', 'y': 'o', 'z': 'p'}

orig_file = open('text.txt', 'r')
file_read = orig_file.read()
orig_file.close()
encry_file = open('encrypted.txt', 'w')

for ch in file_read:
    if ch in encry_library:
        encry_file.write(encry_library[ch])
    else:
        encry_file.write(ch)

encry_file.close()
encry_file = open('text.txt', 'r')
file_read = encry_file.read()
encry_file.close
codes_items = encry_library.items()

for ch in file_read:
    if not ch in encry_library.values() or ch == '.' or ch == '!':
        print(ch)
    else:
        for k, v in codes_items:
            if ch == v and ch != '.':
                print(k, end='')


