#
# Kellen McBurnett
# Apr 5 2025
# Magic 8 Ball Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 
# Make a list with the txt file
with open('Magic-8-Ball/8_ball_responses.txt', 'r') as file:
    response = file.readlines()
import random
# Create a loop
while True:
    # Ask for user input
    question = input('Ask a question of the Magic 8 Ball, or type quit to finish: ')
    # Break the loop if the user types quit
    if question.lower() == 'quit':
        break
    # Give a random response from the list and repeat if the user didn't input quit
    print(random.choice(response))