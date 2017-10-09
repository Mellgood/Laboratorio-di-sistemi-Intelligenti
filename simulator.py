import random
import time
import threading
from tkinter import *


class GUI:
    def __init__(self):
        pass
    def destroy(self):
        self.w.destroy()

    def updateInterface(self,world):
        self.master = Tk()
        self.w = Canvas(self.master, width=800, height=800)
        for i in range(world.height):
            for k in range(world.width):
                if world.matrix[k][i]==0:
                    color="black"
                elif world.matrix[k][i]=="#":
                    color="red"
                else:
                    color="green"
                text=self.w.create_text(50*i + 50, 50*k + 50,  text=world.matrix[k][i], fill=color,font=('Arial',26))
        self.w.pack()
        self.w.update()


class World2D:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.matrix = [ [0 for i in range(self.width)] for j in range(self.height)]
        self.robotList = []
        for i in range(self.height):
            self.matrix[i].insert(random.randint(0, self.width), "#")
            self.matrix[i].insert(random.randint(0, self.width), "#")
        for i in range(self.height):
            randomNumber = random.randint(0, self.width);
            while self.matrix[i][randomNumber] == "#":
                randomNumber = random.randint(0, self.width)
            self.matrix[i].insert(randomNumber, "R" + i.__str__())

    def worldPrint(self):
        for i in range(self.height):
            print(self.matrix[i])

    def makeRobots(self):
        for i in range(self.height):
            for j in range(self.width):
                if(isinstance(self.matrix[i][j], str) and self.matrix[i][j][0] == "R"):
                    rob = Robot(self.matrix[i][j], (i,j),self)
                    self.robotList.append(rob)

    def printRobots(self):
        for r in self.robotList:
            print(r)

    def updateCell(self,pos,value):
        self.matrix[pos[0]][pos[1]]=value

    def getAround(self,pos):
        '''
        extract of the surroundings
        :param pos:coordinate of the central cell form witch we extract the surroundings
        :return: list of surroundings cells
        '''
        out=[]
        if(pos[0]-1<0):
            out.append(('N', "0"))
        else:
            out.append(('N', self.matrix[pos[0] - 1][pos[1]]))
        if (pos[0] + 1 > self.height):
            out.append(('S', "0"))
        else:
            out.append(('S', self.matrix[pos[0] + 1][pos[1]]))
        if (pos[1] - 1 < 0):
            out.append(('W', "0"))
        else:
            out.append(('W', self.matrix[pos[0]][pos[1]-1]))
        if pos[1] - 1 > self.width:
            out.append(('E', "0"))
        else:
            out.append(('E', self.matrix[pos[0]][pos[1]+1]))


        return out


class Robot:
    '''
    Defines how a Robot object is created
    '''
    def __init__(self, name, pos, world=None):
        assert isinstance(name, str)
        assert isinstance(pos, tuple)
        assert len(pos) == 2

        self.name = name
        self.setPosition(pos)
        self.width,self.height=5,5
        self.map = [ [0 for i in range(self.width)] for j in range(self.height)]
        self.myworld =world

    def getPosition(self):
        return self.pos

    def printUserFriendlyPosition(self):
        print("Robot " + self.getName() + " position is " + str(self.getPosition()) + "\n")

    def setPosition(self,pos):
        self.pos=pos

    def getName(self):
        return self.name

    def step(self):
        '''
        This is one step of the robot's life
        :return: None
        '''
        self.sense()
        # self.think()
        # self.act ()

    def sense(self):
        self.perception(self.myworld.getAround(self.pos))

    def __str__(self):
        return self.name + "@" + str(self.pos)

    def perception(self,sensors):
        for s in sensors:
            if s[0] == 'N': self.map[0]=s[1]
            elif s[0] == 'S': self.map[1]=s[1]
            elif s[0] == 'W': self.map[2]=s[1]
            else : self.map[3]=s[1]

    def move(self,direction,world):
        threadLock.acquire(1)
        self.sense()
        newPos=oldPos=self.getPosition()
        direction=str(direction).upper()
        if direction not in ["N","S","E","W"]:
            print("\nWrong direction!")

        if  direction =="N" and self.map[0]==0:
            newPos = (self.pos[0]-1,self.pos[1])
        elif direction =="S" and self.map[1]==0:
            newPos = (self.pos[0] + 1, self.pos[1])
        elif direction == "E" and self.map[2]==0:
            newPos = (self.pos[0], self.pos[1])
        elif direction == "W" and self.map[3]==0:
            newPos = (self.pos[0], self.pos[1])
        else:
            print("\nUnable to move to a not empty location of the map.")
        if newPos[0]==-1 or newPos[1]==-1 or newPos[0] > world.width or newPos[1]>world.height:
            print("\nUnable to move outside of the map.")
            newPos=oldPos

        self.setPosition(newPos)
        world.updateCell(oldPos, 0)
        world.updateCell(newPos, self.name)
        threadLock.release()


threadLock = threading.Lock()
'''
world = World2D(10, 10)
world.worldPrint()
world.makeRobots()

'Creating a GUI, we need the world as argument. Then we sleep to have time to look @ grid.'
g=GUI()
g.updateInterface(world)
time.sleep(5)
r0= world.robotList[0]

'Take a look to robot position before&after the movement'
r0.printUserFriendlyPosition()
r0.move("S",world)
r0.printUserFriendlyPosition()

world.worldPrint()
g.updateInterface(world)
time.sleep(5)
'''