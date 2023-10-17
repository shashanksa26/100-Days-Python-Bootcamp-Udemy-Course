# This is a Python program that calculates the amount each person should pay for a bill, including a
# tip, based on user input. The program prompts the user to enter the total bill amount, the
# percentage of tip they would like to give (10%, 12%, or 15%), and the number of people splitting the
# bill. It then calculates the tip amount, adds it to the bill, and divides the total by the number of
# people to get the amount each person should pay. Finally, it prints out the result in the format
# "Each person should pay : {splitted_bill} RS".
print("Welcome to the Tip Calculator")
bill=float(input("What was the total bill? "))
tip=float(input("What percentage tip would you like to give? 10, 12 or 15? "))
tip_percentage=float(bill/tip)
tipped_bill=float(bill + tip_percentage)
num_people=float(input("How many people to split the bill? "))
splitted_bill=round(tipped_bill/num_people,2)
print(f"Each person should pay : {splitted_bill} RS")