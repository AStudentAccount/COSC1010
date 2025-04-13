#
# Kellen McBurnett
# Apr 13 2025
# Pig Latin Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 
# Define main
def main():
    # Make input and split it into a word list
    words = str(input('Input Sentance: ')).split()
    # "for" loop that cycles through each word in the list
    for word in words: 
        # changes the word(s) to pig latin, prints the words
        print(word[1:] + word[0] + "ay", end = " ")
    print()

# Call main function
main()