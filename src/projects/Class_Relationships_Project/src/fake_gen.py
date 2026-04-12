
from stupid_proofable import *
from character_classes import *
from faker import Faker
import random

def auto_character():
    fake = Faker()
    name = fake.name()
    
    chosen_class = random.randint(1,5)
    
    match chosen_class:
        case 1:
            char = WellRounded(name)
        case 2:
            char = Archer(name)
        case 3:
            char = Warrior(name)
        case 4:
            char = Mage(name)
        case 5:
            char = Engineer(name)
    
    char.packager(char.dictionarize())
    
    #Levels up to a random level 1-4
    levels = random.randint(0,4)
    
    char_info = JSON_reader()[name]
    #Levels up individual stats
    for x in range(levels):
        char_info["Level"] += 1
        stats = char_info["Stats"]
        stats["Defense"] *= 1.25
        stats["Strength"] *= 1.25
        stats["Health"]*=1.25
        stats["Intelligence"]*=1.5
        char_info["Stats"] = stats
    
    #Randomizes armor
    for x in range(random.randrange(0,3)):
        armor_type = random.choice(["Helmet","ChestPlate","Leggings","Boots"])
        defense_value = float(random.randint(1,5))

        char_info["Armor"][armor_type] = defense_value
        char_info["Stats"]["Defense"] += defense_value
    
    JSON_edit(char_info,name)
