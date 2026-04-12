#PS 1st main code

#Import code
from sub_ui import *
from data_visualizing import *
from fake_gen import *

@decorator
def main():
    print("Welcome to the Character Creator\nChoose an Option:\n1. Create New Character\n2. View One Character's Information\n3. Level up Character\n4. Battle Characters\n5. View All Created Characters\n6. Equip/Remove Armor or Weapons from a character\n7. Assign New Abilities (The Weapon the Ability Uses must exist first before the ability can be made)\n8. Use Graphs\n9. Create a Random Character\n10. Exit")
    main_choice = stupid_proofed_inputs("Enter here: ","number","1","2","3","4","5","6","7","8","9")

    match main_choice:
        case "1":
            character_creator()
        case "2":
            view_single()
        case "3":
            level_up()
        case "4":
            #Adds all the characters to the Game to Be used by Battle Mode
            g = Game(JSON_reader().keys())
            g.battle()
            g.clear_characters()
        
        case "5":
            view_all()
        case "6":
            weapons_management()
        case "7":
            create_ability()
        case "8":
            data_ui()
        case "9":
            auto_character()
        case "10":
            print("Type no in exit prompt")

main()