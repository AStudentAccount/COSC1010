#
# Kellen McBurnett
# Apr 12 2025
# Vowels and Consonants Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 
# define main function
def main():
    # Get a string from user
    user_str = input('Enter a string of characters: ')

    # num_function returns the amount of vowels in the string as an argument
    def num_vowels(s): 
        # Make a list of the vowels
        vowels = ['a', 'e', 'i', 'o', 'u']
        # Initialize accumulator
        v_count = 0
        # Count the vowels in s
        for ch in s:
            if ch.lower() in vowels:
                v_count += 1

        # Return the vowel count
        return v_count

    # num_constant returns the amount of vowels in the string as an argument
    def num_constants(s):
        # Make a list containing vowels
        vowels = ['a', 'e', 'i', 'o', 'u']
        # Initialize accumulator
        c_count = 0
        # Count constants in s
        for ch in s:
            if ch.isalpha() and ch.lower() not in vowels:
                c_count += 1
            
        # return the constant count
        return c_count

    # Report Vowels and Constants
    print('That string has', num_vowels(user_str), 'vowels and', num_constants(user_str), 'constants.')

main()