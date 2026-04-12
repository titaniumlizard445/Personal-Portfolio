#PS 1st Fractal patterns generator

import turtle
import math

def stupid_proofed_inputs(message,method,*allowed_inputs):
    while True:
        user_data = ""
        if method == "lower":
            user_data = input(f"\n\n{message}").strip().lower()
        elif method == "title":
            user_data = input(f"\n\n{message}").strip().title()
        elif method == "number":
            while not user_data.isnumeric():
                user_data = input(f"\n\n{message}").strip()
                if not user_data.isnumeric():
                    print("\n\nWrite a number")
        elif method == "none":
            user_data = input(f"\n\n{message}").strip()
        else:
            print("Programmer ERROR: used improper method")
        if user_data in allowed_inputs:
            return user_data
        if "_" in allowed_inputs:
            return user_data
        else:
            print("\n\nYou have inputed something in incorrectly please try again")


#triangle draw-er
def draw_triangle(size,counter=3):
    if counter == 0:
        return
    else:
        draw_triangle(size,counter-1)
        turtle.pendown()
        turtle.forward(size)
        turtle.left(120)
        turtle.penup()

#recurser part
def triangles(depth,size=1024,coords=(-500.0,-500.0)):
    if depth == 0:
        #once smallest of all the corners have been calculated, we go to each of the points calculated and draw a triangle at each
        turtle.goto(coords)
        draw_triangle(size)
        return
    else:
        #This finds where each recursed iteration of triangles goes
        #the ABC calculations find the corners of the bottom left triangle
        A = coords
        B =(list(A)[0]+size/2,list(A)[1])
        C = (list(A)[0]+size/4,list(A)[1]+(size/4)*math.sqrt(3))
        #find points or draw for bottom left triangle
        triangles(depth-1,size/2,A)
        #find points or draw for bottom right triangle
        triangles(depth-1,size/2,B)
        #find points or draw for top middle triangle
        triangles(depth-1,size/2,C)

#koch curve drawer
def draw_bump(depth,size=729):
    #Base case
    if depth==0:
        turtle.forward(size)
    else:
        #draw first flat part
        draw_bump(depth-1,size/3)
        turtle.left(60)
        #draw first part of spike
        draw_bump(depth-1,size/3)
        turtle.right(120)
        #draw second part of spike
        draw_bump(depth-1,size/3)
        turtle.left(60)
        #draw final flat part
        draw_bump(depth-1,size/3)

#snowflake draw-er
def snowflake(depth,sides=3):
    if sides == 0:
        return
    else:
        draw_bump(depth)
        turtle.right(120)
        snowflake(depth,sides-1)

#draw single branch
def drawline(size,coordinate,direction):
    #goes to the base of the branch
    turtle.penup()
    turtle.goto(coordinate)
    turtle.pendown()
    #creates new branch
    turtle.setheading(direction)
    turtle.forward(size)
    #used for future iterations
    coord = turtle.position()
    return coord

#similar system to the sierpinski triangle except we only save the endpoints and draw from there
#tree draw-er
def tree(depth,direction,coord=(0.0,-500.0),size=256):
    new_coord = drawline(size,coord,direction)
    if depth > 0:
        #if you want lobsided trees, the numbers being added and subtracted to find direction can be changed, just make sure they add up to 90 (together)
        direction1 = direction + 45
        direction2 = direction - 45
        #draws left branch
        tree(depth-1,direction1,new_coord,size*(math.sqrt(2)/2))
        #draws right branch
        tree(depth-1,direction2,new_coord,size*(math.sqrt(2)/2))
    else:
        return


#save function
def save(file_name):
    #get the window object and then save it
    turtle.getscreen().getcanvas().postscript(file=f"{file_name}.ps",colormode="color")
    print("File saved as an .PS\nTo change the format, Go to freeconvert.com or some other image converter and then change to desired format\nNote:.PS DOES NOT OPEN THE IMAGE WHEN OPENED")


#turtle setup function to make main shorter
def setup(back_color,turtle_color):
    #setup the turtle
    start_coords = (-500.0,-500.0)
    screen = turtle.Screen()
    screen.bgcolor(back_color)
    turtle.color(turtle_color)
    turtle.penup()
    turtle.goto(start_coords)
    turtle.pendown()
    turtle.speed(0)
    #remove the pound sign before turte.tracer() to make the drawing finished instantly
    #turtle.tracer(0)
    return start_coords


#main function
def main():

    #options for UI (recursion depth, turtle color, background color, save?, fractal type)
    print("Hello and welcome to the turtle graphics fractal generator!\nLets get started with some information:\n\n")
    fractal_type = stupid_proofed_inputs("What type of fractal would you like to use? (options: triangle, snowflake, tree)\nEnter here: ","lower","triangle","snowflake","tree")
    depth = int(stupid_proofed_inputs("How many iterations would you like the fractal to go to? (options: numbers 1-8)\nEnter here:","number","1","2","3","4","5","6","7","8"))
    turtle_color = stupid_proofed_inputs("What is the color you would like the turtle to be? (options: (Rainbow colors),black,white,grey,cyan)\nEnter here: ","lower","red","orange","yellow","green","blue","purple","black","white","grey","cyan")
    back_color = stupid_proofed_inputs("What is the color you would like the background to be?(options: black, white, grey, beige, brown)\nEnter here:","lower","black","white","grey","beige","brown")
    save_ask = stupid_proofed_inputs("Would you like the program to automatically save the fractal for you when it is done drawing it?(options: y (yes), n (no)\nEnter here:","lower","y","n")

    if save_ask == "y":
        save_name = stupid_proofed_inputs("What would you like the file to be named? (options:Any,Note: DO NOT INCLUDE SPACES)\nEnter here:","none","_")

    #setup turtle
    setup(back_color,turtle_color)

    #get the right fractal type
    match fractal_type:
        case "triangle":
            turtle.title("The Amazing Sierpinski Triangle!")
            triangles(depth)
        case "snowflake":
            turtle.title("The Amazing Koch Snowflake")
            turtle.penup()
            turtle.goto(-300,-300)
            turtle.pendown()
            turtle.left(60)
            snowflake(depth)
        case "tree":
            turtle.title("The Tree thing")
            turtle.width(10/depth)
            tree(depth,90)
    
    #saves if the user specifies to do so
    if save_ask == "y":
        save(save_name)
    
    #hide the turtle
    turtle.hideturtle()
    turtle.done()

main()
