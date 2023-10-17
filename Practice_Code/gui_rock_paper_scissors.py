"""
    This is a Python program that allows the user to play Rock-Paper-Scissors against the computer using
    a GUI interface.
    """
import random    
import tkinter as tk
from PIL import Image, ImageTk

# Define the game images
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

# Create the main window
window = tk.Tk()
window.title("Rock-Paper-Scissors")

# Create the image labels
user_image_label = tk.Label(window)
computer_image_label = tk.Label(window)
result_label = tk.Label(window, font=("Arial", 16, "bold"))

# Function to handle user's choice
def play():
    user_choice = int(user_input_entry.get())
    if user_choice >= 3 or user_choice < 0:
        result_label.config(text="You typed an invalid number, you lose!", fg="red")
    else:
        user_image_label.config(text=game_images[user_choice])
        computer_choice = random.randint(0, 2)
        computer_image_label.config(text=game_images[computer_choice])
        if user_choice == 0 and computer_choice == 2:
            result_label.config(text="You win!", fg="green")
        elif computer_choice == 0 and user_choice == 2:
            result_label.config(text="You lose", fg="red")
        elif computer_choice > user_choice:
            result_label.config(text="You lose", fg="red")
        elif user_choice > computer_choice:
            result_label.config(text="You win!", fg="green")
        elif computer_choice == user_choice:
            result_label.config(text="It's a draw", fg="blue")

# Create the user input entry and button
user_input_label = tk.Label(window, text="What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors:", font=("Arial", 16))
user_input_entry = tk.Entry(window, font=("Arial", 16))
play_button = tk.Button(window, text="Play", font=("Arial", 16), command=play)

# Configure the layout using grid
user_input_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
user_input_entry.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
play_button.grid(row=1, column=2, padx=10, pady=10)
user_image_label.grid(row=2, column=0)
computer_image_label.grid(row=2, column=2)
result_label.grid(row=3, column=1, pady=10)

# Display initial welcome message
welcome_label = tk.Label(window, text="Welcome to Rock-Paper-Scissors!", font=("Arial", 20, "bold"))
welcome_label.grid(row=4, column=0, columnspan=3, pady=20)

# Start the main event loop
window.mainloop()
