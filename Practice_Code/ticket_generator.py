print("Welcome to the rollarcoaster!")
age=int(input("What is your age? "))
height=int(input("What is your Height? "))
bill=0
if(height>=120):
    print("You can ride rollarcoaster!")
    if age<12:
        bill=50
        print(" Child tickets 50rs.")
    elif age<=18:
        bill=70
        print("Youth tickets 70rs.")
    elif age<=55 and age>=45:        
        print("Everthing gonna be ok. Have a free ride on us!")
    else:
        bill=120
        print("Adult tickets 120rs.")
    
    wants_pic=input("Do you want a picture to be taken: Y or N ")
    if wants_pic== "Y" or wants_pic=="y" :        
        bill +=30
    print(f"Your final bill is :{bill}")
else:
    print("You can't ride rollarcoaster!")