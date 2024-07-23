import tkinter as tk
from random import randint
from tkinter.colorchooser import askcolor

''' ----- SUPPORTING FUNCTIONS + UNIVERSAL VARIABLES-----'''
#set some universal variables for ease of use
screenDimensions = (screenWidth, screenHeight) = 1200, 650
screenColour = "white"
toolbarWidth = 50
Colour = "black"
selectedShape = "rectangle"
x1 = None
y1 = None

#test function that will draw an oval in a random position
def drawRand():
    x1, y1 = (randint(0,0), randint(0,0))
    x2, y2 = (randint(0, screenWidth - toolbarWidth), randint(0, screenHeight))
    drawingArea.create_oval(x1,y1,x2,y2, fill = Colour)
    return None

#function used to change the shape depending on what button has been pressed most recently
def changeShape(input):
    global selectedShape
    if input == 0:
        selectedShape = "rectangle"
    elif input == 1:
        selectedShape = "oval"
    elif input == 2:
        selectedShape = "line"
    return None

#function that actually draws the shape using user input
def drawShape(event):
    x = event.x
    y = event.y
    global selectedShape
    global x1, y1
    #if no coordinates have already been passed through
    if x1 is None and y1 is None:
        x1 = x
        y1 = y
    else:
        #if x1 and y1 already have coordinates then define x2 and y2 and draw the shape
        x2 = x
        y2 = y

        if selectedShape == "rectangle":
            drawingArea.create_rectangle(x1,y1,x2,y2,fill = Colour) 
        elif selectedShape == "oval":
            drawingArea.create_oval(x1,y1,x2,y2, fill = Colour)
        elif selectedShape == "line":
            drawingArea.create_line(x1, y1, x2,y2, fill = Colour)

        #reset x1 and y1 to none to reset the function
        x1 = None
        y1 = None
    return None

#function used to change the universal variable for colour selection.
def changeColour():
    a = askcolor(title= "Pick your favourite one")
    global Colour 
    Colour = a[1]
    return None

''' -----SETTING THE SCREEN AREAS ----- '''
#define the window
root = tk.Tk()
root.title("RK Paint (this isn't a ripoff of MS Paint you're just imagining things)")
root.config(bg = screenColour)

#Define the canvas are which will be the drawable area
drawingArea = tk.Canvas(root, width=screenWidth - toolbarWidth, height = screenHeight)
drawingArea.pack(side=tk.RIGHT)
drawingArea.bind("<Button-1>", drawShape)

#Declare the buttons
exitButton = tk.Button(root, text="exit", command=lambda : root.quit()).pack(side = tk.BOTTOM)
squareButton = tk.Button(root, text="Rectangle", command=lambda :changeShape(0) ).pack()
ovalButton = tk.Button(root, text="Oval", command = lambda : changeShape(1)).pack()
lineButton = tk.Button(root,text = "Line", command = lambda : changeShape(2)).pack()
colourButton = tk.Button(root, text="Change Colour", command = lambda : changeColour()).pack()

root.mainloop()