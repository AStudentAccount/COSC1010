#
# Kellen McBurnett
# Apr 27 2025
# File Encryption and Decryption Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

# Define Encrypted Library
encry_library = {'A': '!', 'B': '@', 'C': '#', 'D': '$', 'E': '%', 'F': '^', 'G': '&', 'H': '*', 'I': '(', 
                 'J': ')', 'K': 'l', 'L': '_', 'M': '+', 'N': '=', 'O': '{', 'P': '}', 'Q': '[', 'R': ']', 
                 'S': '|', 'T': ';', 'U': ':', 'V': 'r', 'W': '<', 'X': '/', 'Y': '>', 'Z': '?', 'a': 'q', 
                 'b': 'r', 'c': 's', 'd': 't', 'e': 'u', 'f': 'v', 'g': 'w', 'h': 'x', 'i': 'y', 'j': 'z', 
                 'k': 'a', 'l': 'b', 'm': 'c', 'n': 'd', 'o': 'e', 'p': 'f', 'q': 'g', 'r': 'h', 's': 'i', 
                 't': 'j', 'u': 'k', 'v': '"', 'w': 'm', 'x': 'n', 'y': 'o', 'z': 'p'}
# Open text.txt in read mode
orig_file = open('File-Encryption-and-Decryption/text.txt', 'r')
# Read it, close it
file_read = orig_file.read()
orig_file.close()
# Open encrypted.txt in write mode
encry_file = open('File-Encryption-and-Decryption/encrypted.txt', 'w')

# Go through all the characters read
for ch in file_read:
    # Check if it's in the library
    if ch in encry_library:
        # If it is, write the new encrypted character
        encry_file.write(encry_library[ch])
    else:
        # If not, just write the original character
        encry_file.write(ch)

# Close, reread text.txt and close it
encry_file.close()
encry_file = open('File-Encryption-and-Decryption/text.txt', 'r')
file_read = encry_file.read()
encry_file.close

# Get pairs from the library
codes_items = encry_library.items()

# Make a for loop to look through the read content
for ch in file_read:
    # If it's not in the library, print as normal
    if not ch in encry_library.values() or ch == '.' or ch == '!':
        print(ch)
    else:
        # If it doesn't meet the conditions (. or !) look through the pairs
        for k, v in codes_items:
            # Check if they match the value and aren't periods, and if they match, print
            if ch == v and ch != '.':
                print(k, end='')

# Define Decrypted Library
decry_library = {'!': 'A', '@': 'B', '#': 'C', '$': 'D', '%': 'E', '^': 'F', '&': 'G', '*': 'H', '(': 'I', 
                 ')': 'J', 'l': 'K', '_': 'L', '+': 'M', '=': 'N', '{': 'O', '}': 'P', '[': 'Q', ']': 'R', 
                 '|': 'S', ';': 'T', ':': 'U', 'r': 'V', '<': 'W', '/': 'X', '>': 'Y', '?': 'Z', 'q': 'a', 
                 'r': 'b', 's': 'c', 't': 'd', 'u': 'e', 'v': 'f', 'w': 'g', 'x': 'h', 'y': 'i', 'z': 'j', 
                 'a': 'k', 'b': 'l', 'c': 'm', 'd': 'n', 'e': 'o', 'f': 'p', 'g': 'q', 'h': 'r', 'i': 's', 
                 'j': 't', 'k': 'u', '"': 'v', 'm': 'w', 'n': 'x', 'o': 'y', 'p': 'z'}

# Open encrypted.txt in read mode
orig_file = open('File-Encryption-and-Decryption/encrypted.txt', 'r')
# Read it, close it
file_read = orig_file.read()
orig_file.close()
# Open encrypted.txt in write mode
encry_file = open('File-Encryption-and-Decryption/encrypted.txt', 'w')

# Go through all the characters read
for ch in file_read:
    # Check if it's in the library
    if ch in decry_library:
        # If it is, write the new decrypted character
        encry_file.write(decry_library[ch])
    else:
        # If not, just write the original character
        encry_file.write(ch)

# Close, reread text.txt and close it
encry_file.close()
encry_file = open('File-Encryption-and-Decryption/encrypted.txt', 'r')
file_read = encry_file.read()
encry_file.close

# Get pairs from the library
codes_items = decry_library.items()

# Make a for loop to look through the read content
for ch in file_read:
    # If it's not in the library, print as normal
    if not ch in decry_library.values() or ch == '.' or ch == '!':
        print(ch)
    else:
        # If it doesn't meet the conditions (. or !) look through the pairs
        for k, v in codes_items:
            # Check if they match the value and aren't periods, and if they match, print
            if ch == v and ch != '.':
                print(k, end='')