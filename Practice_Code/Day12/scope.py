enemies = 1 #global scope variable

def increase_enemies():
  enemies = 5 #local scope variable
  print(f"enemies inside function: {enemies}")
  
increase_enemies()
print(f"enemies outside function: {enemies}\n") 

print("Second example for the same")
#example 2
player_health=5

def drink_potion():
  potion_strength=10
  print(f"inside player health {player_health}")
drink_potion()
print(f"outside player health {player_health}")