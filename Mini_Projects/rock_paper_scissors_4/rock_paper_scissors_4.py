import random
import msvcrt  # for not terminating the terminal b/w input output buffer

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

ROCK
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

PAPER
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

SCISSORS
'''
game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >= 3 or user_choice < 0: 
    print("You typed an invalid number, you lose!")
else:
    print("You Chose:")
    print(game_images[user_choice])
    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])
    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw")

msvcrt.getch() # this is used to only when we want to exit from the terminal by pressing any key

''' while True:
    key = msvcrt.getch().decode('utf-8').lower()  # Get a key press and decode it
    if key == 'n':
        break ''' # this is used to only keep the terminal open and not to exit
# the msvcrt is used here for the .exe file making using the pyinstaller tool and the library in python
