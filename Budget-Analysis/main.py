#
# Kellen mcBurnett
# Feb 16 2025
# Budget Analysis Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 
# Define Varibales
num = 0.0
tot = 0.0
budget = 0.0
budgetFIN = 0.0

# Display directions for the code
print('Enter your budget this month, followed by any expenses made this month. When done, type "done" into expense.')

# Get budget from user input
budget = int(input('Enter your budget: '))

# Set up a "While" loop for monthly expenses and add them together
while True:
    number = input("Enter expense")
    if number == 'done':
        break
    try :
        num1 = float(number)
    except:
        print('Invalid Input')
        continue
    num = num+1
    tot = tot + num1

# Calculate the total expenses subtracted from the budget
budgetFIN = budget - tot

# Print final budget
print('All done! Your total is $', format(budgetFIN, ',.2f'))