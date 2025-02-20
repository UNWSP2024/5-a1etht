#Programmer: Alethea Lo
#Date: 2/19/25
#Title: Math Quiz

import random

def generate_question():
    """Generates two random numbers and returns their sum."""
    num1 = random.randint(100, 999)
    num2 = random.randint(100, 999)
    correct_answer = num1 + num2
    return num1, num2, correct_answer

#Generate a question for the quiz
num1, num2, correct_answer = generate_question()

#Displaying the question
print(f"  {num1}\n+ {num2}\n------")

#Getting user input
user_answer = int(input("Enter your answer: "))

#Checking if the answer is correct/incorrect
if user_answer == correct_answer:
    print("Congratulations! Your answer is correct.")
else:
    print(f"Incorrect. The correct answer is {correct_answer}.")
