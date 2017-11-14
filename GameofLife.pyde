
import sys
import random
import math


def setup():
    frameRate(10)
    size(1100, 700)
    background(255)
    pixelDensity(displayDensity())

    global onscreen, grid, w, grid2, gridSize
    onscreen = True
    gridSize = 40
    grid = [[0] * gridSize for n in range(gridSize)]
    grid2 = [[0] * gridSize for n in range(gridSize)]

    randomcell()
    w = 20


def randomcell():
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] = random.randint(0, 1)

def drawcubes():
    global onscreen

    if onscreen:
        grid2 = neighbor()
        status(grid2)

    x, y = 0, 0
    grid2 = neighbor()
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                count = grid2[row][col]
                if count == 1:
                    fill(250, 0, 0)
                if count == 2:
                    fill(150, 50, 50)
                if count == 3:
                    fill(50, 100, 100)
                if count == 4:
                    fill(0, 50, 50)
                if count == 5:
                    fill(0, 100, 50)
                if count == 6:
                    fill(0, 200, 50)
                if count == 7:
                    fill(0, 250, 250)
                if count == 8:
                    fill(0, 250, 150)
            else:
                fill(255)
            rect(x, y, w, w)
            x = x + w
        y = y + w
        x = 0

def status(list):
    for i in range(len(list)):
        for j in range(len(list[i])):
            if list[i][j] == 3:
                grid[i][j] = 1
            elif list[i][j] == 2 and grid[i][j] == 1:
                grid[i][j] = 1
            else:
                grid[i][j] = 0


def neighbor():
    count = [[0] * gridSize for n in range(gridSize)]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            count[i][j] = grid[i][j - 1] + grid[i][(j + 1) % len(grid)] + grid[(i + 1) % len(grid)][j] + grid[i - 1][j] + grid[i - 1][j - 1] + grid[i - 1][(j + 1) % len(grid)] + grid[(i + 1) % len(grid)][j - 1] + grid[(i + 1) % len(grid)][(j + 1) % len(grid)]
    return count


def keyPressed():
    global onscreen, grid

    if key == " ":
        if onscreen:
            onscreen = False
        else:
            onscreen = True

    if key == "n":
        for i in range(gridSize):
            for j in range(gridSize):
                grid[i][j] = 0

    if key == "r":
        randomcell()


def mousePressed():
    grid[mouseY / w][mouseX / w] = 1


def draw():
    clear()
    background(255)
    drawcubes()