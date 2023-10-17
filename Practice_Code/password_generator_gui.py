import random
import tkinter as tk
import tkinter.messagebox as messagebox

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+','/','^']

    nr_letters = int(letter_input.get())
    nr_symbols = int(symbol_input.get())
    nr_numbers = int(number_input.get())

    password_list = []
    for char in range(1, nr_letters + 1):
        password_list.append(random.choice(letters))
    for num in range(1, nr_numbers + 1):
        password_list += random.choice(numbers)
    for sym in range(1, nr_symbols + 1):
        password_list += random.choice(symbols)

    random.shuffle(password_list)
    length = len(password_list)

    password = ""
    for char in password_list:
        password += char

    password_text.delete(1.0, tk.END)  # Clear previous password
    password_text.insert(tk.END, password)

def copy_password():
    password = password_text.get(1.0, tk.END).strip()
    if password:
        window.clipboard_clear()
        window.clipboard_append(password)
        messagebox.showinfo("Password Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("No Password", "No password generated yet!")

# Create the main window
window = tk.Tk()
window.title("PyPassword Generator")

# Create input labels and entry fields
letter_label = tk.Label(window, text="How many letters would you like in your password?")
letter_label.pack()
letter_input = tk.Entry(window)
letter_input.pack()

symbol_label = tk.Label(window, text="How many symbols would you like?")
symbol_label.pack()
symbol_input = tk.Entry(window)
symbol_input.pack()

number_label = tk.Label(window, text="How many numbers would you like?")
number_label.pack()
number_input = tk.Entry(window)
number_input.pack()

# Create generate button
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack()

# Create label for displaying the result
password_text = tk.Text(window, height=1, width=30)
password_text.pack()

# Create copy button
copy_button = tk.Button(window, text="Copy Password", command=copy_password)
copy_button.pack()

# Start the GUI event loop
window.mainloop()
