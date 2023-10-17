# This is a Python program that generates a random password based on user input. The program prompts
# the user to enter the number of letters, symbols, and numbers they want in their password. It then
# generates a password by randomly selecting characters from the lists of letters, symbols, and
# numbers, shuffling them, and concatenating them into a string. Finally, it prints the generated
# password to the console.
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+','/','^']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list=[]
for char in range(0,nr_letters):
    password_list.append(random.choice(letters))
for num in range(0,nr_numbers):
    password_list+= random.choice(numbers)
for sym in range(0,nr_symbols):
    password_list+= random.choice(symbols)

random.shuffle(password_list)
length=(len(password_list))

password=""
for char in password_list:
    password+=char
print(f"Your password of length '{length}' is: {password}")