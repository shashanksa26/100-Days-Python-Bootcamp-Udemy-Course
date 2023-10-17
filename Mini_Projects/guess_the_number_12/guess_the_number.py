from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 to 100.")
difficulty=input("Choose a difficulty. Type 'easy' or 'hard': ").lower()


random_number = random.randint(1,100)
print(f"pssst {random_number}")

if difficulty == 'easy':
    attempt = 10
if difficulty == 'hard':
    attempt = 5
print(f"You have {attempt} attempts remaining to guess the number ")
while attempt != 0:
    guessed_num = int(input("Make a guess: "))
    if guessed_num < random_number:
        print("Too low.")
        print("Guess again.")
        attempt -= 1
        print(f"You have {attempt} attempts remaining to guess the number")
    if guessed_num > random_number:
        print("Too High.")
        print("Guess again.")
        attempt -= 1
        print(f"You have {attempt} attempts remaining to guess the number")
    elif guessed_num == random_number:
        print(f"You Got it! the answer was {random_number}.")