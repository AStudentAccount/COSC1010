#
# Kellen McBurnett
# March 16
# Average of Numbers Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 
# Open and read the file (given by user input later)
# Open the file, read it
fileNUM = open('/workspaces/COSC1010/Average-of-Numbers/numbers.txt', 'r')
# Define numbers as 'nums' and make them a list of ints
nums = [int(line) for line in fileNUM]
# Calculate the average
average = sum(nums) / len(nums)
# Close the file
fileNUM.close()
# Print the average
print (f'The average is {average}')
