#PS CP2 personal portfolio project
from custom_styles import *
import customtkinter as ctk
import sub_menus
from projects import Fractal_generator
from projects.Class_Relationships_Project.src.class_rel_main import main2
from projects import JohnJonathanAdventure
from projects import Race_of_the_Turtles

def main():
    root = ctk.CTk()
    root.geometry("1500x1200+0+0")
    ctk.set_appearance_mode("dark")
    root.title("Portfolio")

    foreground = Foreground(root)
    foreground.show()
    
    main_title = Title(foreground.foreground,"Personal Portfolio")
    main_title.show()

    description = Description(foreground.foreground,"Welcome, This Portfolio contains 4 of my best projects I have created.\n The Programs included are: \n \n\n1. Fractal generator\n This Program allows a user to choose from 3 types of fractals (sierpenski triangle, pythagorean tree, and koch snowflake) then turtle will draw the fractal\n \n\n2. Video Game Character Manager\nThis Program allows a user to create compare and battle Video Game Characters\n \n\n3. Text Based Adventure Game\nThis Program is an entire game about the adventure of John Jonathan Johnson\n \n\n4. Turtle Race\n Watch as turtles race across the turtle window to the finish line!\n \n\nTo learn more about these projects, Click on the corresponding button.\n The Project will not run until the 'Run' button is clicked, Then the project will most likely run in the terminal.\nNote: Do not click the run button more than once. If you do it will result in a runtime error. Once a program has started running, it won't stop until it completed it's set task")
    description.show()

    fractal_button = Button(foreground.foreground,"Fractal Generator",lambda:sub_menus.default_UI("Fractal Generator","A Fractal is a patern where a shape repeats ontop of itself a set number of times\n The Fractal Generator Creates The Fractals: Sierpenski Triangle, pythagorean Tree, and Koch Snowflake.\nThe Fractal Generator will ask for information before running. The information is as follows:\n\n1. Type of Fractal\n\n2. Depth (How many layers it generates)\n\n3. Color of the Fractal\n\n4. Background Color\n\n5. If you want to save the image to your computer\n\n This Project will run in the VS code terminal after the 'Run' Button is pressed to the right.",lambda:Fractal_generator.main()))
    fractal_button.show(200,700)

    vgcm_button = Button(foreground.foreground,"Video Game Character Manager",lambda:sub_menus.default_UI("Video Game Character Creator","The Video Game Character Creator Program Allows users to creates DnD like characters, fight, and manage them.\n Some Notable Features in this program are:\n\n1. Creating Characters with random information thanks to Faker \n\n2. Look at character's stats with matplotlib\n\n3. Fight Created Characters\n\n4. Edit and Level Up Characters\n\n5. Saving all of the information to a JSON file\n\nThis program runs in the VS code terminal when the 'Run' button is clicked to the right.",lambda:main2()))
    vgcm_button.show(200,900)

    tba_button = Button(foreground.foreground,"Text Based Adventure Game",lambda:sub_menus.default_UI("Text Based Adventure Game","This Project was the final for Computer Programming 1,\n It contains the epic saga of John Jonathan Johnson and how he defeated the rat king.\n This program works through text so there is no Visuals at all besides text.\n This Program runs in the VS code Terminal. To run the Project click the 'Run' button to the right.",lambda:JohnJonathanAdventure.start_game()))
    tba_button.show(800,700)

    race_button = Button(foreground.foreground,"Turtle Race",lambda:sub_menus.default_UI("Turtle Race","This Program uses python turtles to create and Race on a turtle-created Race Track.\nThis Program runs in a turtle window and winner is displayed in VS code Terminal. To run the Project click the 'Run' button to the right.",lambda:Race_of_the_Turtles.turtles()))
    race_button.show(800,900)

    exit = Exit(foreground.foreground,root.destroy)
    exit.show()

    root.mainloop()

main()