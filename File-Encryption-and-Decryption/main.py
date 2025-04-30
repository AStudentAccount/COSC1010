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
# Open text.txt and read it
file = open('text.txt', 'r')
orig_text = file.read()
# Assign encry_txt an empty string
encry_txt = ""
# Open a for loop with all the keys in the original text
for key in orig_text:
    # Update the empty string with the keys from the dictionary
    encry_txt += encry_library.get(key, key)
    # Open the new file and write into it with the updated keys
    encry_file = open('encrypted.txt', 'w')
    encry_file.write(encry_txt)

# Define Decrypted Library
decry_library = {'!': 'A', '@': 'B', '#': 'C', '$': 'D', '%': 'E', '^': 'F', '&': 'G', '*': 'H', '(': 'I', 
                 ')': 'J', 'l': 'K', '_': 'L', '+': 'M', '=': 'N', '{': 'O', '}': 'P', '[': 'Q', ']': 'R', 
                 '|': 'S', ';': 'T', ':': 'U', 'r': 'V', '<': 'W', '/': 'X', '>': 'Y', '?': 'Z', 'q': 'a', 
                 'r': 'b', 's': 'c', 't': 'd', 'u': 'e', 'v': 'f', 'w': 'g', 'x': 'h', 'y': 'i', 'z': 'j', 
                 'a': 'k', 'b': 'l', 'c': 'm', 'd': 'n', 'e': 'o', 'f': 'p', 'g': 'q', 'h': 'r', 'i': 's', 
                 'j': 't', 'k': 'u', '"': 'v', 'm': 'w', 'n': 'x', 'o': 'y', 'p': 'z'}

# Open encrypted.txt and read it
file = open('encrypted.txt', 'r')
orig_text = file.read()
# Assign encry_txt an empty string
encry_txt = ""
# Open a for loop with all the keys in the original text (this time encrypted.txt)
for key in orig_text:
    # Update the empty string with the keys from the dictionary
    encry_txt += decry_library.get(key, key)
    # Open encrypted.txt and write into it with the updated keys
    encry_file = open('encrypted.txt', 'w')
    encry_file.write(encry_txt)