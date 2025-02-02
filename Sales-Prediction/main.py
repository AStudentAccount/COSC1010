#
# Kellen McBurnett
# Sun, Feb 2
# Sales Prediction Programming Project
# COSC 1010
#

# Variables to hold the sales total and the profit
#sales total is determined by input
#profit is sales muliplied by 23% (0.23)

# Get the amount of projected sales.
total_sales = float(input('Enter the projected sales: '))
# Calculate the projected profit.
profit = total_sales*0.23
# Print the projected profit.
print('The profit is $', format(profit, ',.2f'))