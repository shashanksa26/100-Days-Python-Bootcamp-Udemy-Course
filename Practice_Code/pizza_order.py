print("Welcome to Python pizza Delivery!!")
size=input("What size of pizza you want? S,M or L: ")
add_pepperoni=input("Do you want pepporoni? Y or N: ")
extra_cheese=input("Do you want extra cheese? Y or N: ")
small_pizza_rs=15
medium_pizza_rs=20
large_pizza_rs=25
pepperoni_small_rs=2
pepperoni_rest_rs=3
extra_cheese_rs=1
bill=0
if size=="S":
    bill+=small_pizza_rs
    if add_pepperoni=="Y":
        bill+=pepperoni_small_rs
    if extra_cheese=="Y":
        bill+=extra_cheese_rs
if size=="M":
    bill+=medium_pizza_rs
    if add_pepperoni=="Y":
        bill+=pepperoni_rest_rs
    if extra_cheese=="Y":
        bill+=extra_cheese_rs
if size=="L":
    bill+=large_pizza_rs
    if add_pepperoni=="Y":
        bill+=pepperoni_rest_rs
    if extra_cheese=="Y":
        bill+=extra_cheese_rs
print(f"Total bill is: ${bill}")