#
# Kellen McBurnett
# Feb 8 2025
# Hot Dog Cookout Calculator Programming Project
# COSC 1010
#

# Constants.
HOT_DOGS_PER_PACKAGE = 10
BUNS_PER_PACKAGE = 8

# Local Variables.
numAttending = 0    # Number of people attending.
numPerPerson = 0    # Numbers of hot dogs and buns per person.
total = 0           # Total hot dogs and buns needed.
minDogs = 0         # Minimum of hot dog packages required.
minBuns = 0         # Minimum of bun packages required.
dogsLeft = 0        # Leftover hot dogs.
bunsLeft = 0        # Leftover buns.

# Get the number of people attending the cookout via user input.
numAttending = int(input('Enter the number of people attending the cookout: '))

# Get the number of hot dogs per person via user input.
numPerPerson = int(input('Enter the number of hot dogs per person: '))

# Calculate the total number of hot dogs and buns needed.
total = numAttending * numPerPerson

# Calculate the minimum number of packages of hot dogs needed.
minDogs = total // HOT_DOGS_PER_PACKAGE

# Determine if the number of people attending is large enough to require more than one package of hot dogs.
if minDogs > 0:
    # Calculate the number of the hot dogs left over from the package, if any.
    dogsLeft = total % HOT_DOGS_PER_PACKAGE

    # If there will be leftovers, add an additional package of hot dogs.
    if dogsLeft != 0:
        minDogs += 1

# Set the minimum number of packages of hot dogs to one, because the number of people attending is small enough to require only one package of hot dogs
else:
    minDogs = 1

# Determine, if any, the number of leftover hot dogs
dogsLeft = (HOT_DOGS_PER_PACKAGE * minDogs) - total

## Bun Section
# Calculate the minimum number of packages of buns needed.
minBuns = total // BUNS_PER_PACKAGE

# Determine if the number of people attending is large enough to require more than one package of buns.
if minBuns > 0:
    # Calculate the number of buns left over from the package, if any.
    bunsLeft = total % BUNS_PER_PACKAGE

    # If there will be leftovers, add an additional package of buns.
    if bunsLeft != 0:
        minBuns += 1

# Set the minimum number of packages of buns to one, because the number of people attending is small enough to require only one package of buns
else:
    minBuns = 1

# Determine, if any, the number of leftover buns
bunsLeft = (BUNS_PER_PACKAGE * minBuns) - total

# Display the minimum of hot dog packages needed
print('Minimum packages of hot dogs needed: ', minDogs)

# Display the minimum of bun packages needed
print('Minimum packages of buns needed: ', minBuns)

# Display the number of hot dogs left over
print('Hot dogs left over: ', dogsLeft)

# Display the number of hot dogs left over
print('Buns left over: ', bunsLeft)