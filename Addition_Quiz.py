# Program 2: Addition Quiz
# Create a program that automatically generate two random numbers to add (0 to 99)
# Let the user answer and evaluate if the user has the correct answer
# The program will ask the user 10 addition operation
# Display the result summary of the 10 operations (ex 9/10)

import random

def random_numbers_sum_score():
    score_count = 0
    score_limit = 0

    num1 = random.randint(0, 99)
    num2 = random.randint(0, 99)
    print(f"First number: {num1}")
    print(f"Second number: {num2}")

random_numbers_sum_score()