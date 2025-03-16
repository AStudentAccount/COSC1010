#
# Kellen McBurnett
# March 16 
# File Display Programming Project
# COSC 1010
#
# Open the file
myfile = open('/workspaces/COSC1010/File-Display/numbers.txt', 'r')
# Read and display file's contents
for line in myfile:
    number = int(line)
    print(number)

# Close the file
myfile.close()