import math
import sys

#Script to calculate the amount of times you need to cast a copy spell before a single "kill" spell (such as lightning bolt or brain freeze) will win the game
#Command line execution should be formatted: python3 mtg_copy_win_calc.py copy_num Spell#1 dmg Spell#1 players Spell#1 life Spell#2 dmg Spell#2 players Spell#2 life... and so on
#copy_num is the number of times the copy spell copies future spell casts
#dmg is the amount of "damage" the kill spell does, this can be non-traditional damage such as mill or poison counters
#players is the amount of players the kill spell affects, generally will be 1 for targeted spells or 3 for "other players" spells
#life is the amount of "damage" needed to be done to kill one player with the spell, generally 40 for damage, 100 for mill, 10 for poison, etc
#all arguments should be integers

#function that does all of the calculations, returns the number of times the copy spell needs to be cast before the kill spell is lethal to the whole table
def calc_casts(copy_num, dmg, players, life):
    #spell needs to do enough damage to kill each player, so we take the amount of damage the spell needs for a kill and multiply it by the amount of times it needs to be repeated for each player
    dmg_needed = life * (4 - players)
    #we need to make enough copies of our kill spell to do greater than or equal our opponents "life" so we always round up
    spells_needed = math.ceil(dmg_needed / dmg)
    copy_casts = 0
    #the amount of copies of our kill spell we will get is equal to number of copies our copy spell makes to the power of the amount of times we've cast our copy spell
    #for example, if we have cast Bonus Round twice and then cast lightning bolt, we get 2^2 = 4 lightning bolts (it will technically make 3 copies+1 original)
    curr_spells = copy_num ** copy_casts
    #we keep casting our copy spell until we have at least as many kill spell copies we need
    while(curr_spells < spells_needed):
        copy_casts += 1
        curr_spells = copy_num ** copy_casts
    #return the number of times we need to cast our copy spells to do at least as much damage as needed to kill the table
    return copy_casts
 
def main():
    args = sys.argv
    arg_len = len(args)
    #check to see if there is the correct number of arguments, each spell has 3 arguments, plus one for the number of copies and one for the script name, so we see if the num of args-2 is divisible by 3
    if (arg_len-2) % 3 != 0:
        sys.exit("Incorrect number of arguments, please include the number of copies your copy spell makes, then for each spell include the \"damage\" it does, the number of players it affects, and how much damage per player it must do. \nFor example: python3 mtg_copy_win_calc.py 2 3 1 40 1 3 40 3 1 100")
    spell_num = (arg_len-2) / 3
    #i is the spell number we are on (starting at 1), j is the index of the spell we are working on, starting on 2 since 0 is irrelevant and 1 is the spell copy number
    i = 1
    j = 2
    #keep going until we've gone through all the spells
    while(i <= spell_num):
        #since there are 3 arguments per spell, j is the dmg, j+1 is the players, and j+2 is the life
        print("Spell " + str(i) + ": " + str(calc_casts(int(args[1]), int(args[j]), int(args[j+1]), int(args[j+2]))) + " casts")
        #go on to the next spell, j increases by 3 since +1 and +2 are just the second and third arguments of the last spell
        i+=1
        j+=3
if __name__ == "__main__":
    main()