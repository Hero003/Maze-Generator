import math
import tkinter as tk
import random

def displayCells(grid):

    global currentCell 
    global stackCells

    canvas.delete("all")

    currentCell.isVisited = True

    for cell in grid:
        if cell.isVisited:
            x1, y1, x2, y2 = cell.showDetails()
            canvas.create_rectangle(x1, y1, x2, y2, fill = "purple", outline = "")



    x1, y1, x2, y2 = currentCell.showDetails()
    canvas.create_rectangle(x1, y1, x2, y2, fill = "green", outline = "")

    for cell in grid:
        x1, y1, x2, y2 = cell.showDetails()
        walls = cell.checkWalls()

        if walls[0]:
            #Wall 1 - Top wall
            canvas.create_line(x1, y1, x2, y1, fill = "white")

        if walls[1]:
            #Wall 2 - Right wall
            canvas.create_line(x2, y1, x2, y2, fill = "white")

        if walls[2]:
            #Wall 3 - Bottom wall
            canvas.create_line(x2, y2, x1, y2, fill = "white")

        if walls[3]:
            #Wall4 - Left wall
            canvas.create_line(x1, y2, x1, y1, fill = "white")


    
    nextCell = currentCell.checkNeighbors()

    if nextCell:

        nextCell.isVisited = True

        stackCells.append(currentCell)

        RemoveWalls(currentCell, nextCell)

        currentCell = nextCell
    
    elif  len(stackCells) > 0:

        currentCell = stackCells.pop()
    


    root.after(1, displayCells, grid) # so we set this 

def RemoveWalls(currentCell, nextCell):

    x = currentCell.i - nextCell.i

    if x == -1:

        currentCell.wallsExist[2] = False
        nextCell.wallsExist[0] = False

    if x == 1:

        currentCell.wallsExist[0] = False
        nextCell.wallsExist[2] = False

    y = currentCell.j - nextCell.j

    if y == -1:

        currentCell.wallsExist[1] = False
        nextCell.wallsExist[3] = False


    if y == 1:

        currentCell.wallsExist[3] = False
        nextCell.wallsExist[1] = False


    

def index(i, j):

    if i < 0 or  j < 0 or i > mazeRows - 1 or j > mazeCols - 1:

        return -1
    
    return i * mazeCols + j

#Cell Object
class Cell:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.wallsExist = [True, True, True, True] #A list contain booleans for if walls exist
#                           Top,Right, Bottom, Left
        self.isVisited = False
        self.neighbours = [0, 0, 0, 0] # A list ocntaining indices of all the nieghbouring cells
#                           Top,Right, Bottom, Left

    def showDetails(self):
        x1 = self.j * cellSize
        x2 = x1 + cellSize
        y1 = self.i * cellSize
        y2 = y1 + cellSize

        return x1, y1, x2, y2
    
    def checkNeighbors(self):

        notVisited = []

        topIndex = index((self.i - 1), self.j)
        rightIndex = index(self.i, (self.j + 1))
        bottomIndex = index((self.i + 1), self.j)
        leftIndex = index(self.i, (self.j - 1))

        self.neighbours = [topIndex, rightIndex, bottomIndex, leftIndex]        

        if  topIndex != -1 and not grid[topIndex].isVisited:
           notVisited.append(grid[topIndex])

        if  rightIndex != -1 and not grid[rightIndex].isVisited:
           notVisited.append(grid[rightIndex])

        if  bottomIndex != -1 and not grid[bottomIndex].isVisited:
           notVisited.append(grid[bottomIndex])

        if  leftIndex != -1 and not grid[leftIndex].isVisited:
           notVisited.append(grid[leftIndex])

        if len(notVisited) > 0:

            randomInt = random.randint(0, (len(notVisited) - 1))
            return notVisited[randomInt]

        else:

            return None
    
    def checkWalls(self):
        return self.wallsExist

#-------------#------------#-------------#------------#------------#------------#------------#------------#------------#------------#------------#------------

# Root window setup
root = tk.Tk()
root.title("Maze Generator")

windowWidth = 600
windowHeight = 600
root.geometry(str(windowWidth) + "x" + str(windowHeight))

#Setting up the canvas
canvas = tk.Canvas(root, width = windowWidth, height = windowHeight, bg = "black")
canvas.pack(fill = "both", expand = True)

cellSize = 20

mazeRows = math.floor(windowHeight / cellSize)
mazeCols = math.floor(windowWidth / cellSize)

grid = [] #A one dimensional list to contain all the cells in the maze

for i in range(0, mazeRows, 1):
    for j in range(0, mazeCols, 1):
        cell = Cell(i, j)
        grid.append(cell)

currentCell = grid[0]

stackCells = []

displayCells(grid)

















root.mainloop()