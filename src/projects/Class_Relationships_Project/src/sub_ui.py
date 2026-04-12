#PS 1st CP2 UI stuff

#get class stuff
from .character_classes import *
#get stoobid proofing funcs
from .stupid_proofable import *
#get JSON manipulation funcs
from .files.file_management import *


#character chooser for smaller code size
def char_chooser():
    character_info = JSON_reader()
    characters = character_info.keys()
    
    for x in characters:
        print(f"{x}")

    user_choice = stupid_proofed_inputs("\n\nEnter here: ","none","_")

    while user_choice not in characters:
        user_choice = stupid_proofed_inputs("\n\nEnter here: ","none","_")
    return user_choice


#UI for Character Creator
def character_creator():
    #info from user inputs needed: Name, Class - Class makes a bunch of defaults like abilities, stats and weapons
    print("\n\n========= CHARACTER CREATOR =========\n\n")
    print("Create a new character\n\n")
    
    name = stupid_proofed_inputs("Enter the name of the character here: ","none","_")
    
    print("\n\nClasses\n1. Well Rounded\n2. Archer\n3. Warrior\n4. Mage\n5. Engineer")
    
    chosen_class = stupid_proofed_inputs("Enter Class here: ","number","1","2","3","4","5")
    
    match chosen_class:
        case "1":
            char = WellRounded(name)
        case "2":
            char = Archer(name)
        case "3":
            char = Warrior(name)
        case "4":
            char = Mage(name)
        case "5":
            char = Engineer(name)
    
    char.packager(char.dictionarize())


#Level One Character Up
def level_up():
    print("\n\n============= LEVEL UP CHARACTER ================\n\n")
    print("Choose a Character to level up")
    
    character_info = JSON_reader()
    user_choice = char_chooser()

    #Levels up individual stats
    char_info = character_info[user_choice]
    char_info["Level"] += 1
    stats = char_info["Stats"]
    stats["Defense"] *= 1.25
    stats["Strength"] *= 1.25
    stats["Health"]*=1.25
    stats["Intelligence"]*=1.5
    char_info["Stats"] = stats

    JSON_edit(char_info,user_choice)


    print(f"\n\nCharacter Leveled Up Sucessfully, Level:{character_info[user_choice]["Level"]}")


#View Single Character
def view_single():
    print("================ Single Character Stats ===================")
    
    characters = JSON_reader()
    user_choice = char_chooser()
    
    print("================ CHARACTER STATS ================")
    print(f"Name: {user_choice}\nDefense: {characters[user_choice]["Stats"]["Defense"]}\nStrength: {characters[user_choice]["Stats"]["Strength"]}\nHP: {characters[user_choice]["Stats"]["Health"]}\nIntelligence: {characters[user_choice]["Stats"]["Intelligence"]}\nLevel: {characters[user_choice]["Level"]}\nClass: {characters[user_choice]["Class"]}")
    
    print("Weapons:")
    for x in characters[user_choice]["Weapons"]:
        print(x)
    
    print(f"ARMOR:\nHelmet:{characters[user_choice]["Armor"]["Helmet"]}\nChestPlate: {characters[user_choice]["Armor"]["ChestPlate"]}\nLeggings: {characters[user_choice]["Armor"]["Leggings"]}\nBoots: {characters[user_choice]["Armor"]["ChestPlate"]}")
    
    print("Inventory (Non Weapons or Armor)")
    for x in characters[user_choice]["Inventory"]:
        print(x)
    
    print("Abilities")
    for x in characters[user_choice]["Abilities"].keys():
        print(f"{x}:{characters[user_choice]["Abilities"][x]["Description"]}")


#View All Characters
def view_all():
    characters = JSON_reader().keys()
    for x in characters:
        print(x)


#Create Abilities
def create_ability():
        print("\n\n======== Ability Maker ========\n\n")
        
        print("Which Character would you like to assign this ability to?")
        character_assigned = char_chooser()

        char = JSON_reader()[character_assigned]

        name = stupid_proofed_inputs("What is the name of the ability you want to create?\nEnter here: ","none","_")
        description = stupid_proofed_inputs("Please write a detailed description for what your abilty does here: ","none","_")
        
        item_used = stupid_proofed_inputs("What is the item that this ability uses? (if none Enter Basic)(Item will be added to the inventory of the character that this ability is assigned to)\nEnter here: ","none","_")
        while item_used not in char["Weapons"] and item_used not in char["Inventory"]:
            print(f"\n\nThis Character does not have Item: {item_used}, Please Try Again\n\n")
            item_used = stupid_proofed_inputs("What is the item that this ability uses? (if none Enter Basic)(Item will be added to the inventory of the character that this ability is assigned to)\nEnter here: ","none","_")
        
        damage_delt = stupid_proofed_inputs("How much damage does this ability do?\nEnter here: ","number","_")
        
        
        info = JSON_reader()
        info[character_assigned]["Abilities"][name] = {"Damage":damage_delt,"Description":description,"ItemUsed":item_used}
        JSON_edit(info[character_assigned],character_assigned)


#Add and remove Items
def weapons_management():
    print("\n\n========== Item Management =============\n\n")

    print("Choose a Character:")
    choice = char_chooser()
    
    #useful things
    item_type = stupid_proofed_inputs("\n\nWhat Inventory Would You like to Change? \n1.Weapons\n2.Armor\n3.Items\nEnter here:","number","1","2","3")
    add_remove = stupid_proofed_inputs("\n\nWould you like to add an item or remove it? (Add,Remove)\nEnter here: ","title","Add","Remove")
    char = JSON_reader()[choice]
    
    if add_remove == "Remove":
        match item_type:
            case "1":
                weapons = JSON_reader()[choice]["Weapons"]
                for x in weapons:
                    print(f"Weapon: {x}")

                to_remove = stupid_proofed_inputs("Which Weapon would you like to remove?\nEnter here: ","none","_")
                weapons.remove(to_remove)

                char["Weapons"] = weapons
        
            case "2":
                armor = JSON_reader()[choice]["Armor"]
                
                print("Which Armor would you like to remove?")
                armor_available = []

                #determines if there is any armor
                if armor["Helmet"] != None:
                    print("Helmet is Equipped")
                    armor_available.append("Helmet")
                
                if armor["ChestPlate"] != None:
                    print("ChestPlate is Equipped")
                    armor_available.append("ChestPlate")
                
                if armor["Leggings"] != None:
                    print("Leggings are Equipped")
                    armor_available.append("Leggings")
                
                if armor["Boots"] != None:
                    print("Boots are Equipped")
                    armor_available.append("Boots")
                
                if armor_available == []:
                    print("\n\nYou Have No Armor so you can't remove something you don't have.\n\n")
                else:
                    #Extra Layer of Stupid Proofing
                    to_unequip = stupid_proofed_inputs("\nEnter here: ","title","Chestplate","Helmet","Leggings","Boots")
                    while to_unequip not in armor_available:
                        print(f"\n\nCan't Unequip {to_unequip} Please Try Again\n\n")
                        to_unequip = stupid_proofed_inputs("Enter here: ","title","Chestplate","Helmet","Leggings","Boots")

                    #this does the exchange of armor taking off and removing defense earned by the armor
                    defense = armor[to_unequip]
                    armor[to_unequip] = None
                    char["Armor"] = armor
                    char["Stats"]["Defense"] -= defense
        
            case "3":
                items = JSON_reader()[choice]["Inventory"]
                for x in items:
                    print(f"Item: {x}")
                
                to_remove = stupid_proofed_inputs("\n\nWhich Item would you like to remove?\nEnter here: ","none","_")
                items.remove(to_remove)
                char["Invetory"] = items
        
    elif add_remove == "Add":
        match item_type:
            case "1":
                weapon_added = stupid_proofed_inputs("\n\nWhat is the name of the weapon you would like to add?\nEnter here: ","none","_")
                char["Weapons"].append(weapon_added)
            case "2":
                armor_type = stupid_proofed_inputs("\n\nWhat type of armor would you like to add? (if armor is already used, it is replaced by new value)\nEnter here:","title","Helmet","ChestPlate","Leggings","Boots")
                defense_value = float(stupid_proofed_inputs(f"\n\nHow much defense does {armor_type} yield? (number)(recommend below 10)\nEnter here:","number","_"))

                char["Armor"][armor_type] = defense_value
                char["Stats"]["Defense"] += defense_value

            case "3":
                item_to_add = stupid_proofed_inputs("\n\nWhat is the name of the weapon you would like to add?\nEnter here: ","none","_")
                char["Inventory"].append(item_to_add)
    else:
        print("\n\nNot a Valid Option")

    JSON_edit(char,choice)
                