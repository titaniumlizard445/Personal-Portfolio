#PS 1st CP2 Insert Game and Character classes here

import random
from stupid_proofable import *
from files.file_management import *

#Use agregation for Game to Characters
class Game:
    def __init__(self,characters = []):
        self.characters = characters
    
    def add_character(self,character):
        self.characters.append(character)
    
    def __str__(self):
        print(self.characters)
    
    def clear_characters(self):
        self.characters = []
    
    def battle(self):
        print("Choose First Fighter\n\n")
        
        character_info = JSON_reader()
        characters = character_info.keys()
        
        for x in characters:
            print(x)
        
        #chooser
        first = stupid_proofed_inputs("\n\nEnter here: ","none","_")
        while first not in characters:
            print("Not Valid Character, Please Try Again")
            first = stupid_proofed_inputs("\n\nEnter here: ","none","_")
        
        print("Choose Second Fighter\n\n")
        
        second = stupid_proofed_inputs("\n\nEnter here: ","none","_")
        while second not in characters:
            print("Not Valid Character, Please Try Again")
            second = stupid_proofed_inputs("\n\nEnter here: ","none","_")
        
        first_info = character_info[first]
        second_info = character_info[second]
        first_health = first_info["Stats"]["Health"]
        second_health = second_info["Stats"]["Health"]
        
        print("========== THE BATTLE COMENCETH ===========")
        while first_health != 0 and second_health != 0:
            #P1 Turn
            if first_health != 0 and second_health != 0:
                
                print(f"{first}'s Turn")
                print("\n\nChoose an Ability:")
                
                first_abilities = first_info["Abilities"].keys()
                for x in first_abilities:
                    print(x)

                print("Weapons available: ")
                for x in first_info["Weapons"]:
                    print(x)
                
                print("Items Available: ")
                for x in first_info["Inventory"]:
                    print(x)

                print("\n\nNote: Abilites cannot be used without proper item\n\n")
                
                ability_chosen = stupid_proofed_inputs("Enter here: ","none","_")
                while ability_chosen not in first_abilities:
                    print("Not Valid Ability, Please Try Again")
                    ability_chosen = stupid_proofed_inputs("Enter here: ","none","_")
                
                while first_info["Abilities"][ability_chosen]["ItemUsed"] not in first_info["Weapons"] and first_info["Abilities"][ability_chosen]["ItemUsed"] not in first_info["Items"]:
                    print("You do not have the Item Neccessary to use this ability, Please Try again")
                    ability_chosen = stupid_proofed_inputs("Enter here: ","none","_")
                
                damage = (int(first_info["Abilities"][ability_chosen]["Damage"])+random.randint(1,25)+first_info["Stats"]["Strength"])-second_info["Stats"]["Defense"]
                second_health -= damage
                
                if second_health < 0:
                    second_health = 0
                
                print(f"{first} did {damage} damage! {second} Health: {second_health}")
            
            #P2 Turn
            if first_health != 0 and second_health != 0:
                
                print(f"{second}'s Turn")
                print("\n\nChoose an Ability:")
                
                second_abilities = second_info["Abilities"].keys()
                for x in second_abilities:
                    print(x)
                
                print("Weapons available: ")
                for x in second_info["Weapons"]:
                    print(x)
                
                print("Items Available: ")
                for x in second_info["Inventory"]:
                    print(x)
                
                print("\n\nNote: Abilites cannot be used without proper item\n\n")

                ability_chosen = stupid_proofed_inputs("Enter here: ","none","_")
                while ability_chosen not in second_abilities:
                    print("Not Valid Ability, Please Try Again")
                    ability_chosen = stupid_proofed_inputs("Enter here: ","none","_")
                
                while second_info["Abilities"][ability_chosen]["ItemUsed"] not in second_info["Weapons"] and second_info["Abilities"][ability_chosen]["ItemUsed"] not in second_info["Items"]:
                    print("You do not have the Item Neccessary to use this ability, Please Try again")
                    ability_chosen = stupid_proofed_inputs("Enter here: ","none","_")
                 
                damage = (int(second_info["Abilities"][ability_chosen]["Damage"])+random.randint(1,25)+second_info["Stats"]["Strength"])-first_info["Stats"]["Defense"]
                first_health -= damage
                
                if first_health < 0:
                    first_health = 0
                
                print(f"{second} did {damage} damage! {first} Health: {first_health}")
        
        print("\n\n========= THE BATTLE ENDETH ==========\n\n")

        if first_health == 0:
            print(f"{second} won!")
        
        elif second_health == 0:
            print(f"{first} won!")

#Methods to be in the Game class: Battle, Display All Characters, Level Up system

#Use Inheritance for characters being a class classes needed: Well rounded (Has all base stats), Archer, Warrior, Mage, Engineer

class DefaultCharacter:
    def __init__(self,name):
        self.name = name

    #send info to JSON
    def packager(self,Character):
        JSON_add({self.name:Character})



#Package all of the info for stats and stuff
class WellRounded(DefaultCharacter):
    def __init__(self,name):
        self.name = name
        self.level = 0
        self.inventory = []
        self.abilities = {"Sword Stike":{"Damage":20,"Description":"Use your sword to deal 20 damage to the other enemy before defense is counted","ItemUsed":"Sword"}}
        self.armor = {
            "Helmet":None,
            "ChestPlate":None,
            "Leggings":None,
            "Boots":None
        }
        self.weapons = ["Sword","Basic"]
        self.player_class = "Well Rounded"
        self.stats = {
            "Defense":7,
            "Strength":5.0,
            "Health":120,
            "Intelligence":10
        }
    
    def dictionarize(self):
        diction = {
            "Abilities":self.abilities,
            "Inventory":self.inventory,
            "Armor":self.armor,
            "Weapons":self.weapons,
            "Class":self.player_class,
            "Level":self.level,
            "Stats":self.stats,
            }
        return diction


class Archer(DefaultCharacter):
    def __init__(self,name):
        self.name = name
        self.level = 0
        self.inventory = []
        self.abilities = {"Arrow Shot":{"Damage":15,"Description":"Use your Bow to deal 15 damage to the enemy before defense is counted","ItemUsed":"Bow"}}
        self.armor = {
            "Helmet":None,
            "ChestPlate":None,
            "Leggings":None,
            "Boots":None
        }
        self.weapons = ["Bow","Basic"]
        self.player_class = "Archer"
        self.stats = {
            "Defense":7,
            "Strength":4.0,
            "Health":100,
            "Intelligence":20
        }
    
    def dictionarize(self):
        diction = {
            "Abilities":self.abilities,
            "Inventory":self.inventory,
            "Armor":self.armor,
            "Weapons":self.weapons,
            "Class":self.player_class,
            "Level":self.level,
            "Stats":self.stats,
            }
        return diction


class Warrior(DefaultCharacter):
    def __init__(self,name):
        self.name = name
        self.level = 0
        self.inventory = []
        self.abilities = {"Claymore Stike":{"Damage":30,"Description":"Use your Claymore to deal 30 damage to the other enemy before defense is counted","ItemUsed":"Clamore"}}
        self.armor = {
            "Helmet":None,
            "ChestPlate":None,
            "Leggings":None,
            "Boots":None
        }
        self.weapons = ["Claymore","Basic"]
        self.player_class = "Warrior"
        self.stats = {
            "Defense":10,
            "Strength":7.0,
            "Health":150,
            "Intelligence":5
        }
    
    def dictionarize(self):
        diction = {
            "Abilities":self.abilities,
            "Inventory":self.inventory,
            "Armor":self.armor,
            "Weapons":self.weapons,
            "Class":self.player_class,
            "Level":self.level,
            "Stats":self.stats,
            }
        return diction


class Mage(DefaultCharacter):
    def __init__(self,name):
        self.name = name
        self.level = 0
        self.inventory = []
        self.abilities = {"Icicle Strike":{"Damage":15,"Description":"Use your sword to deal 20 damage to the other enemy before defense is counted","ItemUsed":"Staff"}}
        self.armor = {
            "Helmet":None,
            "ChestPlate":None,
            "Leggings":None,
            "Boots":None
        }
        self.weapons = ["Staff","Basic"]
        self.player_class = "Mage"
        self.stats = {
            "Defense":3,
            "Strength":3.0,
            "Health":120,
            "Intelligence":30
        }
    
    def dictionarize(self):
        diction = {
            "Abilities":self.abilities,
            "Inventory":self.inventory,
            "Armor":self.armor,
            "Weapons":self.weapons,
            "Class":self.player_class,
            "Level":self.level,
            "Stats":self.stats,
            }
        return diction

class Engineer(DefaultCharacter):
    def __init__(self,name):
        self.name = name
        self.level = 0
        self.inventory = ["Metal"]
        self.abilities = {"Sentry shot":{"Damage":30,"Description":"Build a sentry to deal 30 damage to the other enemy before defense is counted","ItemUsed":"Wrench"}}
        self.armor = {
            "Helmet":None,
            "ChestPlate":None,
            "Leggings":None,
            "Boots":None
        }
        self.weapons = ["Wrench","Basic"]
        self.player_class = "Engineer"
        self.stats = {
            "Defense":4,
            "Strength":7.0,
            "Health":100,
            "Intelligence":50
        }
    
    def dictionarize(self):
        diction = {
            "Abilities":self.abilities,
            "Inventory":self.inventory,
            "Armor":self.armor,
            "Weapons":self.weapons,
            "Class":self.player_class,
            "Level":self.level,
            "Stats":self.stats,
            }
        return diction