#PS CP2 Classes for styles

import customtkinter as ctk


class Foreground:
    def __init__(self, root):
        self.root = root
        self.foreground = ctk.CTkFrame(
            master=root,
            border_width=4,
            corner_radius=10,
            border_color="grey",
            fg_color="lightblue",
            width=1400,
            height=1100
        )
    
    def show(self):
        self.foreground.pack(padx=10,pady=20,fill="both",expand=True)



class Title:
    def __init__(self,foreground,text):
        self.fg = foreground
        self.title = ctk.CTkLabel(
            master=foreground,
            width=500,
            height=60,
            corner_radius=10,
            fg_color="white",
            text_color="black",
            text=text,
            font=ctk.CTkFont(family="Arial",size=50,weight="bold")
        )
    
    def show(self):
        self.title.pack(pady=20)
        


class Description:
    def __init__(self,foreground,text):
        self.fg = foreground
        self.descript = ctk.CTkLabel(
            master=foreground,
            width=800,
            height=500,
            corner_radius=10,
            fg_color="lightgreen",
            text=text,
            text_color="black",
            font=ctk.CTkFont(family="Arial",size=18,weight="normal")
        )
    
    def show(self,position=None):
        if position == None:
            self.descript.pack(pady=20)
        else:
            self.descript.place(x=position[0],y=position[1])
            self.descript.propagate(False)


class Button:
    def __init__(self,foreground,text,command):
        self.root = foreground
        self.button = ctk.CTkButton(
            master=foreground,
            width=400,
            height=150,
            corner_radius=10,
            border_width=5,
            text=text,
            command=command
        )
    
    def show(self,positionx,positiony):
        self.button.place(x=positionx,y=positiony)
        self.button.propagate(False)


class Exit:
    def __init__(self,foreground,command):
        self.root = foreground
        self.button = ctk.CTkButton(
            master=foreground,
            width=200,
            height=50,
            corner_radius=5,
            border_width=5,
            text="Exit",
            command=command,
            fg_color="red",
            text_color="black"
        )
    
    def show(self):
        self.button.place(x=1200,y=10)
        self.button.propagate(False)