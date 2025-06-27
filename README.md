# MTG Spell Copy Win Calculator  
A script to calculate the amount of times you need to cast a copy spell in order to win the game with only one follow up spell  
Command line execution should be formatted: python3 mtg_copy_win_calc.py copy_num Spell#1 dmg Spell#1 players Spell#1 life Spell#2 dmg Spell#2 players Spell#2 life... and so on  
copy_num is the number of times the copy spell copies future spell casts  
dmg is the amount of "damage" the kill spell does, this can be non-traditional damage such as mill or poison counters  
players is the amount of players the kill spell affects, generally will be 1 for targeted spells or 3 for "other players" spells  
life is the amount of "damage" needed to be done to kill one player with the spell, generally 40 for damage, 100 for mill, 10 for poison, etc  
all arguments should be integers  
