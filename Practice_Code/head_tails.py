import random
print("Welcome to Head and Tails tossing !!")
choice=input('What\'s your choice? Type "Head" or "Tails" ')
random_generator=random.randint(0,1)
if random_generator==1:
    print("Heads")
else:
    print("Tails")
