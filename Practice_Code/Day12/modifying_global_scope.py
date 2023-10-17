enemies = 1 #global scope variable

def increase_enemies():
  global enemies #modyfying the variable which is outside
  enemies += 5 #local scope variable
  print(f"enemies inside function: {enemies}")
  
increase_enemies()
print(f"enemies outside function: {enemies}\n") 