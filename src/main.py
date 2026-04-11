#PS CP2 personal portfolio project
from custom_styles import *
import customtkinter as ctk

def main():
    root = ctk.CTk()
    root.geometry("1500x1200+0+0")
    ctk.set_appearance_mode("dark")
    root.title("Portfolio")

    foreground = Foreground(root)
    foreground.show()
    
    main_title = Title(foreground.foreground,"Personal Portfolio")
    main_title.show()

    description = Description(foreground.foreground,"Welcome, This Portfolio contains 4 of my best projects I have created.\n The Programs included are: \n \n\n1. Fractal generator\n This Program allows a user to choose from 3 types of fractals (sierpenski triangle, pythagorean tree, and koch snowflake) then turtle will draw the fractal\n \n\n2. Video Game Character Manager\nThis Program allows a user to create compare and battle Video Game Characters\n \n\n3. Text Based Adventure Game\nThis Program is an entire game about the adventure of John Jonathan Johnson\n \n\n4. Turtle Race\n Watch as turtles race across the turtle window to the finish line!\n \n\nTo learn more about these projects, Click on the corresponding button.\n The Project will not run until the 'Run' button is clicked, Then the project will most likely run in the terminal")
    description.show()

    fractal_button = Button(foreground.foreground,"Fractal Generator",lambda:print("Fractal Clicked"))
    fractal_button.show(200,700)

    vgcm_button = Button(foreground.foreground,"Video Game Character Manager",lambda:print("VG clicked"))
    vgcm_button.show(200,900)

    tba_button = Button(foreground.foreground,"Text Based Adventure Game",lambda:print("TBAG clicked"))
    tba_button.show(800,700)

    race_button = Button(foreground.foreground,"Turtle Race",lambda:print("Turtle Race Clicked"))
    race_button.show(800,900)

    exit = Exit(foreground.foreground,root.destroy)
    exit.show()

    root.mainloop()

main()