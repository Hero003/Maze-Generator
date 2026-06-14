import math
import tkinter as tk

# Root window setup
root = tk.Tk()
root.title("Maze Generator")

root.geometry("400x400")


#Setting up the canvas
canvas = tk.Canvas(root, width=400, height=400, bg = "black")
canvas.pack(fill = "both", expand = True)

cellWidth = 20
cellHeight = 20

x1, x2, y1, y2 = 0, 0, 0, 0

walls_exist = [True, True, True, True] #A list contain booleans for if walls exist
#              Top,Right, Bottom, Left

#To mark a cell as visited
visited = False

for i in range(0, math.floor(400/cellHeight), 1):

    y2 = y1 + cellHeight

    for j in range(0, math.floor(400/cellWidth), 1):

        x2 = x1 + cellWidth


        #We managed to create a cell, but we need to create a cell in such a way that the walls are individually drawn 
        #canvas.create_rectangle(x1, y1, x2, y2, fill = "black", outline = "white")

        if walls_exist[0]:
            #Wall 1 - Top wall
            canvas.create_line(x1, y1, x2, y1, fill = "white")

        if walls_exist[1]:
            #Wall 2 - Right wall
            canvas.create_line(x2, y1, x2, y2, fill = "white")

        if walls_exist[2]:
            #Wall 3 - Bottom wall
            canvas.create_line(x2, y2, x1, y2, fill = "white")

        if walls_exist[3]:
            #Wall4 - Left wall
            canvas.create_line(x1, y2, x1, y1, fill = "white")

        x1 = x2
    
    y1 = y2
    x1, x2 = 0, 0

root.mainloop()
