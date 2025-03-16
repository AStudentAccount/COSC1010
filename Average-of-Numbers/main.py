#
# Kellen McBurnett
# March 16
# Average of Numbers Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 
# Open and read the file (given by user input later)
def file_average(filename):
    file = open(filename, 'r')
    number_list = file.readlines
    # Set total
    total = 0
    # Make a loop to go through the number list
    for number in number_list:
        # Calculate the numbers as a sum and close the file
        total = total + float(number)
    file.close()

# Find the average via division of the total by the number of numbers
    return total / len(number_list)

# Get the File Name from user input
input_filename = input("File: ")
average = file_average(input_filename)

# Print the average
print("Average: ", average)
