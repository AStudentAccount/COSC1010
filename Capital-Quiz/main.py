#
# Kellen McBurnett
# Apr 20 2025
# Capital Quiz Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

def main():

    print('Welcome to the State Capital Quiz! ')

    # Initilaize varibales to keep count of correct and incorrect anwsers
    correct_responses = 0
    incorrect_responses = 0
    # Define states as a list
    states = list(states_and_capitals.keys())
    
    # While loop
    while True:
        # Select random and coinciding state from dictionary
        state = random.choice(states)
        capital = states_and_capitals[state]
        
        # Ask for user input
        user_anwser = input(f'What is the captial of {state}? (Type quit to exit) ').strip().lower()
        
        # Break upon quit
        if user_anwser.lower() == 'quit':
            break
        
        # Correct response, add an correct response count
        if user_anwser == capital.lower():
            print('Correct!')
            correct_responses +=1 
        
        # Incorrect response, add an incorrect response count
        else:
            print(f'Incorrect. The correct answer is {capital}.')
            incorrect_responses += 1
    
    # Print quiz results upon "quit"
    print('\nQuiz Results: ')
    print(f'Correct anwsers: {correct_responses}')
    print(f'Incorrect anwsers: {incorrect_responses}')
    
    
# Initialize dictionary
import random

states_and_capitals = {
            'Alabama':'Montgomery', 'Alaska':'Juneau',
                'Arizona':'Phoenix', 'Arkansas':'Little Rock',
                'California':'Sacramento', 'Colorado':'Denver',
                'Connecticut':'Hartford', 'Delaware':'Dover',
                'Florida':'Tallahassee', 'Georgia':'Atlanta',
                'Hawaii':'Honolulu', 'Idaho':'Boise',
                'Illinois':'Springfield', 'Indiana':'Indianapolis',
                'Iowa':'Des Moines', 'Kansas':'Topeka',
                'Kentucky':'Frankfort', 'Louisiana':'Baton Rouge',
                'Maine':'Augusta', 'Maryland':'Annapolis',
                'Massachusetts':'Boston', 'Michigan':'Lansing',
                'Minnesota':'Saint Paul', 'Mississippi':'Jackson',
                'Missouri':'Jefferson City', 'Montana':'Helena',
                'Nebraska':'Lincoln', 'Nevada':'Carson City',
                'New Hampshire':'Concord', 'New Jersey':'Trenton',
                'New Mexico':'Santa Fe', 'New York':'Albany',
                'North Carolina':'Raleigh', 'North Dakota':'Bismarck',
                'Ohio':'Columbus', 'Oklahoma':'Oklahoma City',
                'Oregon':'Salem', 'Pennsylvania':'Harrisburg',
                'Rhode Island':'Providence', 'South Carolina':'Columbia',
                'South Dakota':'Pierre', 'Tennessee':'Nashville',
                'Texas':'Austin', 'Utah':'Salt Lake City',
                'Vermont':'Montpelier', 'Virginia':'Richmond',
                'Washington':'Olympia', 'West Virginia':'Charleston',
                'Wisconsin':'Madison', 'Wyoming':'Cheyenne'
        }

main()