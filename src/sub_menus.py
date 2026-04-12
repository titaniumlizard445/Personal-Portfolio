#PS CP2 Sub UI menus

import customtkinter as ctk
from custom_styles import *

def default_UI(project_name,description,program):
    root = ctk.CTk()
    root.geometry("1500x1200+0+0")
    root.title(project_name)
    ctk.set_appearance_mode("dark")
    
    fg = Foreground(root)
    fg.show()

    name = Title(fg.foreground,project_name)
    name.show()

    desc = Description(fg.foreground,description)
    desc.show((100,200))

    exit = Exit(fg.foreground,root.destroy)
    exit.show()

    run_button = Button(fg.foreground,"Run",program)
    run_button.show(600,800)

    root.mainloop()
