#
# Kellen McBurnett
# Mar 29 2025
# Exception Handling Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 
#  
# Set a try clause
try: 
    # Open the file, read it
    with open('numbers.txt', "r") as file:
        lines = [line.rstrip() for line in file]
# Define numbers as 'nums' and make them a list of ints
    nums = [int(line) for line in file]
# Calculate the average
    average = sum(nums) / len(nums)
# Close the file
    file.close()
# Print the average
    print (f'The average is {average}')

# Except clause for IOE Errors, which prints an error message if detected
except IOError: 
    print ('An IOError occured.')

# Except clause for Value Errors, which prints an error message if detected
except ValueError:
    print('A ValueError occured.')