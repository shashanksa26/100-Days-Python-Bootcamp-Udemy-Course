import random
from hangman_art import stages, logo
from hangman_words import word_list

print(logo[0])
end_of_game =False
chosen_word=random.choice(word_list)
word_length=len(chosen_word)
lives=6

display=[]
for _ in range(word_length):
    display += "_"

# `while not end_of_game:` is a loop that will continue to run as long as the variable `end_of_game`
# is `False`.
while not end_of_game:
    guess=input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for pos in range(word_length):        
        letter=chosen_word[pos]
        if letter==guess:
            display[pos]=letter
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life ")
        lives -=1
        if lives ==0:
            end_of_game= True
            print("You lose.")
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game=True
        print("You win!!")
    print(stages[lives])