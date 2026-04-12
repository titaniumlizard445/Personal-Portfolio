from .files.file_management import *
import pandas as panda
import matplotlib as plotting
import matplotlib.pyplot as plt
import math
from .sub_ui import *


#Charts: Pie for Class Distribution, Radar for Stats, Bar for Damage per ability

#Statistical Analyzer Chops up data into bites for DataVis
class StatisticalAnalyzer:
    def __init__(self,character_name):
        self.char_name = character_name
        self.char_info = JSON_reader()

    def class_distribution(self):        
        classes_created = []
        for x in self.char_info.keys():
            classes_created.append(self.char_info[x]["Class"])
        
        number_of_c = []
        number_of_c.append(classes_created.count("Well Rounded"))
        number_of_c.append(classes_created.count("Archer"))
        number_of_c.append(classes_created.count("Warrior"))
        number_of_c.append(classes_created.count("Mage"))
        number_of_c.append(classes_created.count("Engineer"))

        used_classes = []
        count = 0
        for x in number_of_c:
            count+=1
            if x > 0:
                match count:
                    case 1:
                        used_classes.append("Well Rounded")
                    case 2:
                        used_classes.append("Archer")
                    case 3:
                        used_classes.append("Warrior")
                    case 4:
                        used_classes.append("Mage")
                    case 5:
                        used_classes.append("Engineer")
            else:
                used_classes.append("")

        return number_of_c, used_classes


    def stats(self):
        char_stats = self.char_info[self.char_name]["Stats"]
        fixed_stats = {
            "Defense":[char_stats["Defense"]],
            "Strength":[char_stats["Strength"]],
            "Health":[char_stats["Health"]],
            "Intelligence":[char_stats["Intelligence"]]
        }
        info = panda.DataFrame(fixed_stats)
        return info, char_stats


    def power_of_ability(self):
        abilities = self.char_info[self.char_name]["Abilities"]
        abil_names = list(abilities.keys())
        abil_damages = []
        
        for x in abil_names:
            abil_damages.append(int(abilities[x]["Damage"]))
        
        info = {
            "Damages":abil_damages,
            "Names":abil_names
        }

        frame = panda.DataFrame(info)

        return frame




class DataVis(StatisticalAnalyzer):
    def __init__(self,char_name=None):
        self.char_info = JSON_reader()
        self.char_name = char_name

    def pie(self):
        plt.pie(self.class_distribution()[0],labels=self.class_distribution()[1])
        plt.title("Distribution of Classes")
        plt.show()
        

    def radar(self):
        data, char_stats = self.stats()

        categories = list(char_stats.keys())
        values = list(char_stats.values())

        number_of_vars = len(categories)
        angles = []
        
        #find the radian distance to distance each axis
        for x in range(number_of_vars):
            angle_for_axis = 2 * math.pi * x / number_of_vars
            angles.append(angle_for_axis)
        
        
        values += values[:1]
        angles += angles[:1]
        
        fig, ax = plt.subplots(figsize=(6,6), subplot_kw=dict(polar=True))
        
        #outline
        ax.plot(angles, values, color="blue", linewidth=2)
        ax.fill(angles, values, color="blue", alpha=0.25)

        #labels for each axis
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(categories)
        
        #display
        plt.title(f"Stat Distribution for {self.char_name}",size=12, y=1.1)
        plt.show()

    def bar(self):
        
        fig, ax = plt.subplots()

        info = self.power_of_ability()
        
        abil_damages = info["Damages"]
        abil_names = info["Names"]

        ax.bar(abil_names, abil_damages,color="blue")

        ax.set_title("Ability Damage Comparison")
        ax.set_ylabel("Damage")
        plt.show()
        

def data_ui():
    print("\n\n=============== Data Vis ================\n\n")
    print("Welcome to the data visualization center, options for visualization\n1. Pie chart to show class distribution for all created classes\n2. Radar Chart to show a characters stats\n3. Bar Chart to compare a character's abilities")
    choice = stupid_proofed_inputs("Enter here: ","number","1","2","3")

    match choice:
        case "1":
            print("Here is your Pie Chart: ")
            obj = DataVis()
            obj.pie()
        case "2":
            print("Here is Your Radar Chart: ")
            char = char_chooser()
            obj = DataVis(char)
            obj.radar()
        case "3":
            print("Here is your Bar Graph: ")
            char = char_chooser()
            obj = DataVis(char)
            obj.bar()
