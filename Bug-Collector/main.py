#
# Kellen McBurnett
# Feb 16, 2025
# Bug Collector Programming Project
# COSC 1010
#
# Initialize variables for bugs and total number of bugs collected.
total = 0
bugs = 0
days = 0

# Get number of bugs collected each day using a for loop.
for day in range (1, 6):
    # Prompt user input
    print('Enter the bugs collected on day', day)

    # Input the number of bugs
    bugs = int(input())
    total += bugs

# Display the total number of bugs collected.
print('You collected a total of', total, 'bugs.')