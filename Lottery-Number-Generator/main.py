#
# Kellen McBurnett
# Mar 29 2025
# Lottery Number Generator Programming Project
# COSC 1010
#
# Use comments liberally throughout the program.
# 
# Define start, end, and max number of digits
MAX_DIGITS = 7
START = 0
END = 9

# Import random function between  start and end
import random 

# Main fuunction
def main():
    # Create a list
    numbers = [0] * 7
    # Fill the list with random numbers
    for index in range(MAX_DIGITS):
        numbers[index] = random.randint (START, END)
    # Display the random numbers
    print('Here are your lottery numbers: ')
    for index in range(MAX_DIGITS):
        print(numbers[index], end='')
    print()
# Call the main function
main()