import random
from spelllist_by_level import spelllist


def getmaxspell(wizlevel):
    """ determine the highest level spells a wizard of level wizlevel would have access to"""
    spellarray = {}
    spelllevel = (wizlevel+1)//2
    #accounts for highest spell level being 9, not 10
    if spelllevel == 10:
        spelllevel = 9
    for level in range(1,spelllevel + 1):
        #magicmath determines the number of spells per level a wizard of level wizlevel would likely have, and accounts 
        #for the wizard level progression and learning spells as they adventure etc
        magicmath = (1/(level/wizlevel))/1.1
        #a wizard starts with 6 level 1 spells, this is taken care of here
        if level == 1:
            magicmath += 6
        spellarray.update({level:round(magicmath)})
    return spellarray

def getspells(number, level):
    """ return a list of spells, length number, of spell level level"""
    spells = []
    levelspelllist = spelllist[level]
    for i in range(number):
        choice = random.choice(levelspelllist)

        if choice in spells:
            #if the spell is in the list, there is a chance of adding it as a personlized spell,
            #otherwise will look for a new original spell of level
            personalized_choice = f"Personalized {choice}"
            if personalized_choice not in spells and bool(random.getrandbits(1)):
                choice = personalized_choice
            else:
                while choice in spells:
                    choice = random.choice(levelspelllist)

        spells.append(choice)

    assert sorted(spells) == sorted(list(set(spells))), f"DUPLICATED SPELL IN {sorted(spells)}"

    return spells
        
        
def spellbook(wizlevel):
    """generate the actual spellbook"""
    spellbook = {}
    spellarray = getmaxspell(wizlevel)
    for key in spellarray:
        value = spellarray[key]
        spellbook.update({key:getspells(value,key)})
    return(spellbook)

while True:
    lev = input("What level wizard spellbook: ")
    test = spellbook(int(lev))
    for line in test:
        print(line)
        print(", ".join(test[line]))
