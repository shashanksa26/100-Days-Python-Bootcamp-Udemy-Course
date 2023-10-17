from art import *
import random
from game_data import data
import os
#display game logo
print(logo)

def format_data(account):
    '''Takes the account data and returns the printable format.'''
    account_name=account["name"]
    account_descr=account["description"]
    account_country=account["country"]
    return(f"{account_name}, a {account_descr}, from {account_country}") 

def check_answer(guess,a_followers,b_followers):
    '''Takes the user guess and follower counts and returns if they got it right.'''
    if a_followers > b_followers:
        return guess=="a"
    else:
        return guess=="b"
score=0
game_should_continue=True
account_b=random.choice(data)
#make the game repeatable 
while game_should_continue:
    #generate a random account from the game data.

    #Making account at position B become the next account at position A
    account_a=account_b
    account_b=random.choice(data)
    
    while account_a== account_b:
        account_b=random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    guess=input("Who has more followers? type 'A' or 'B': ").lower()

    # get the follower count of each account
    a_follower_count=account_a["follower_count"]
    b_follower_count=account_b["follower_count"]
    is_correct= check_answer(guess, a_follower_count,b_follower_count)

    #Clear Screen between rounds:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)

    #Give user feedback on their guess:
    if is_correct:
        score+=1
        print(f"You''re right!! Current score is {score}.")
    else:
        game_should_continue=False
        print(f"Sorry that's wrong. Final score:{score}.")