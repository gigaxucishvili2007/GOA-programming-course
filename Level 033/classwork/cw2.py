"""2)sum all parameters <3
def calculate_damage(opening_attack, core_damage, finishing_move):
    
---> "wizzard new life is SUMED_CALCULATED"
calculate_damage(10, 20, 30)"""

def calculate_damage(opening_attack, core_damage, finishing_move):
    return opening_attack + core_damage + finishing_move
print(calculate_damage(10,20,30))