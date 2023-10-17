string = input("Enter the num to be checked: ")
reverse_string = string[::-1]
print(reverse_string)
if reverse_string == string:
    print(f"num {string} is palindrome")
else:
    print(f"num {string} is not a palindrome")