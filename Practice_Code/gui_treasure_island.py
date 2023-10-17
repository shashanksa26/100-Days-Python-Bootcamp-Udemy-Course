import tkinter as tk
from tkinter import messagebox

def show_message(message):
    messagebox.showinfo("Game Message", message)

def start_game():    
    show_message(''' 
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
 ''')
    show_message("Welcome to Treasure Island.\nYour mission is to find the treasure.")

    def on_left_click():
        

        choice2_window()

    def on_right_click():
        show_message("You fell into a hole. GAME OVER!!")
        

    def choice1_window():
        window = tk.Toplevel(root)
        window.title("Choose a Path")
        window.geometry("300x150")
        window.configure(bg="black")

        label = tk.Label(window, text="You're at a crossroad, where do you want to go?", fg="white", bg="black")
        label.pack(pady=10)

        left_button = tk.Button(window, text="Left", command=on_left_click)
        left_button.pack(pady=5)

        right_button = tk.Button(window, text="Right", command=on_right_click)
        right_button.pack(pady=5)

    def on_wait_click():
        choice3_window()

    def on_swim_click():
        show_message("You got attacked by an angry trout. GAME OVER!!")

    def choice2_window():
        window = tk.Toplevel(root)
        window.title("Lake Adventure")
        window.geometry("300x150")
        window.configure(bg="black")

        label = tk.Label(window, text="You've come to a lake.\nThere is an island in the middle of the lake.", fg="white", bg="black")
        label.pack(pady=10)

        wait_button = tk.Button(window, text="Wait for a boat", command=on_wait_click)
        wait_button.pack(pady=5)

        swim_button = tk.Button(window, text="Swim across", command=on_swim_click)
        swim_button.pack(pady=5)

    def on_red_click():
        show_message("It's a room full of fire. GAME OVER!!")

    def on_yellow_click():
        show_message("You found treasure! You win!!")

    def on_blue_click():
        show_message("You entered a room full of beasts. GAME OVER!!")

    def choice3_window():
        window = tk.Toplevel(root)
        window.title("Choose a Door")
        window.geometry("300x150")
        window.configure(bg="black")

        label = tk.Label(window, text="You arrive at the island unharmed.\nThere is a house with 3 doors.", fg="white", bg="black")
        label.pack(pady=10)

        red_button = tk.Button(window, text="Red", command=on_red_click)
        red_button.pack(pady=5)

        yellow_button = tk.Button(window, text="Yellow", command=on_yellow_click)
        yellow_button.pack(pady=5)

        blue_button = tk.Button(window, text="Blue", command=on_blue_click)
        blue_button.pack(pady=5)

    # Main game window
    root = tk.Tk()
    root.title("Treasure Island Game")
    root.configure(bg="black")

    # Game title label
    title_label = tk.Label(root, text="Treasure Island", font=("Arial", 24, "bold"), fg="white", bg="black")
    title_label.pack(pady=20)

    # Start button
    start_button = tk.Button(root, text="Start Game", font=("Arial", 16), command=choice1_window)
    start_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    start_game()
