import pygame
import sys
import math
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os


col = 50
w = 750 / col
row = 50
h = 750 / row
grids = [0 for x in range(col)]
openSet = []
closedSet = []
red = (255, 51, 51)
green = (0, 255, 0)
blue = (0, 0, 255)
grey = (220, 220, 220)
light_blue = (204, 255, 255)
cameFrom = []


window = Tk()
label = Label(window, text="Start(x-point, y-point): ")
labelEnd = Label(window, text="End(x-point, y-point): ")
startBox = Entry(window)
endBox = Entry(window)
var = IntVar()
showPath = ttk.Checkbutton(window, text="The Steps ", onvalue=1, offvalue=0, variable=var)


# Visual Screen

vScreen = pygame.display.set_mode((750, 750))


class Square:
    # The node square

    def __init__(self,xval, yval):

        self.x = xval       # X axis
        self.y = yval       # Y axis
        self.f = 0          # F value
        self.g = 0          # G value
        self.h = 0          # H value
        # F = G + H
        self.neighbor = []
        self.last = None
        self.obs = False
        self.close = False
        self.val = 1

    def show(self, colour, st):
        # Draw the square

        if self.close is False:
            pygame.draw.rect(vScreen, colour, (self.x * w, self.y * h, w, h),st)
            pygame.display.update()

    def path(self, colour, st):
        # The path finding square

        pygame.draw.rect(vScreen, colour, (self.x * w, self.y * h, w, h),st)
        pygame.display.update()

    def addNeighbor(self, grids):
        x = self.x
        y = self.y
        if x < col-1 and grids[self.x + 1][y].obs is False:
            self.neighbor.append(grids[self.x + 1][y])
        if x > 0 and grids[self.x - 1][y].obs is False:
            self.neighbor.append(grids[self.x - 1][y])
        if y < row-1 and grids[self.x][y + 1].obs is False:
            self.neighbor.append(grids[self.x][y + 1])
        if y > 0 and grids[self.x][y - 1].obs is False:
            self.neighbor.append(grids[self.x][y - 1])


# Draw 2d Array
for x in range(col):
    grids[x] = [0 for x in range(row)]


# Create squares
for x in range(col):
    for y in range(row):
        grids[x][y] = Square(x, y)

# Default initial and target node

start = grids[3][5]
end = grids[12][5]

# Show squares
for x in range(col):
    for y in range(row):
        grids[x][y].show(light_blue, 1)

for x in range(0, row):
    grids[0][x].show(blue, 0)
    grids[0][x].obs = True
    grids[col - 1][x].obs = True
    grids[col - 1][x].show(blue, 0)
    grids[x][row - 1].show(blue, 0)
    grids[x][0].show(blue, 0)
    grids[x][0].obs = True
    grids[x][row-1].obs = True


def submit():
    global start
    global end
    st = startBox.get().split(",")
    ed = endBox.get().split(",")
    start = grids[int(st[0])][int(st[1])]
    end = grids[int(ed[0])][int(ed[1])]
    window.quit()
    window.destroy()


Start = Button(window, text="Start", command=submit)

showPath.grid(columnspan=2, row=2)
Start.grid(columnspan=2, row=3)
labelEnd.grid(row=1, pady=3)
endBox.grid(row=1, column=1, pady=3)
startBox.grid(row=0, column=1, pady=3)
label.grid(row=0, pady=3)


window.update()
mainloop()

pygame.init()
openSet.append(start)


def mousePressed(val):

    # Wall between two points is defined with mousePress

    t = val[0]
    w = val[1]
    g1 = t // (750 // col)
    g2 = w // (750 // row)
    access = grids[g1][g2]
    if access != start and access != end:
        if access.obs is False:
            access.obs = True
            access.show((255, 255, 255), 0)


end.show((255,8,127), 0)
start.show((255,8,127), 0)

looping = True

while looping:

    # Draw wall and after pressing space run the program
    # Wall is white
    event = pygame.event.get()

    for ev in event:
        if ev.type == pygame.QUIT:
            pygame.quit()

        if pygame.mouse.get_pressed()[0]:
            try:
                position = pygame.mouse.get_pos()
                mousePressed(position)
            except AttributeError:
                pass

        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_SPACE:
                looping = False
                break

# Add all neighbours

for x in range(col):
    for y in range(row):
        grids[x][y].addNeighbor(grids)

# H value for F = G + H


def h_value(num, ex):
    dist = math.sqrt((num.x - ex.x)**2 + (num.y - ex.y)**2)
    return dist


def main():
    end.show((255, 8, 127), 0)
    start.show((255, 8, 127), 0)

    if len(openSet) > 0:
        lowIndex = 0
        for x in range(len(openSet)):
            if openSet[x].f < openSet[lowIndex].f:
                lowIndex = x

        currentVal = openSet[lowIndex]

        if currentVal == end:
            print("Finished ", currentVal.f)
            start.show((255,8,127), 0)
            temp = currentVal.f

            for x in range(round(currentVal.f)):
                currentVal.closed = False
                currentVal.show((204, 0, 204), 0)
                currentVal = currentVal.last
            end.show((255, 8, 127), 0)

            Tk().wm_withdraw()
            result = messagebox.askokcancel("Program Done", ('The program done, the shortest distance \n to the path is ' + str(temp) + ' squares away, \n Would you like to reset the program?'))

            if result is True:
                os.execl(sys.executable, sys.executable, *sys.argv)

            else:
                ag = True
                while ag:
                    event = pygame.event.get()
                    for eve in event:
                        if eve.type == pygame.KEYDOWN:
                            ag = False
                            break

            pygame.quit()

        openSet.pop(lowIndex)
        closedSet.append(currentVal)

        neighbor = currentVal.neighbor

        for n in range(len(neighbor)):
            neigh = neighbor[n]

            if neigh not in closedSet:
                tempGvalue = currentVal.g + currentVal.val

                if neigh in openSet:
                    if neigh.g > tempGvalue:
                        neigh.g = tempGvalue

                else:
                    neigh.g = tempGvalue
                    openSet.append(neigh)

            neigh.h = h_value(neigh, end)
            neigh.f = neigh.g + neigh.h

            if neigh.last is None:
                neigh.last = currentVal

    if var.get():
        for i in range(len(openSet)):
            openSet[i].show(green, 0)

        for i in range(len(closedSet)):
            if closedSet[i] != start:
                closedSet[i].show(red, 0)

    currentVal.closed = True


while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        pygame.quit()
    pygame.display.update()
    main()



