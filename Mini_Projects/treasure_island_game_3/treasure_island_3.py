# The `print()` function is used to display a multi-line string that represents an ASCII art of the
# game's title. The rest of the code is a text-based adventure game that prompts the user to make
# choices and displays different outcomes based on those choices.
print(''' 
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
 ''')
print("Welcome to Treasure Island.")
print("Your mission to find the treasure.")
choice1=input('You\'re at a crossroad, where you want to go? Type "left" or "right". :')
choice1_lower=choice1.lower()
if choice1_lower== "left":
    choice2=input('You\'ve come to a lake. Thereis an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. :' ).lower()
    if choice2=="wait":
        choice3=input("You arrive at the island unharmed. There is a house with 3 doors. one red, one yellow and one blue. Which color do you choose? :").lower()
        if choice3=="red":
            print("it's a room full of fire. GAME OVER!!")
        elif choice3=="yellow":
            print("You found treaure! You win!! ")
        elif choice3=="blue":
            print("You entered a room full of beasts. GAME OVER!!")
        else:
            print("You chose a door that doesn't exist. GAME OVER!!")
    else:
        print("You got attacked by n angry trout. GAME OVER!!")
else:
    print("You fell into a hole. GAME OVER!! ")
