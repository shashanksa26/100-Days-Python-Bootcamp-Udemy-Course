'''In this as the variable is inside the conditional statement if so it is not making local scope as it can be accessible outside the statement too in printing.. so the block scope is not valid
only inside the function the variable ,class, function is considered as the local scope
'''

level=3
enemies=['skeleton','zombies','dragon']
if level<5:
    new_enemy=enemies[0]
print(new_enemy)

