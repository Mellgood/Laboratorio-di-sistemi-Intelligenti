import random

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

    def getAround(self,pos):
        '''
        extract of the surroundings
        :param pos:coordinate of the central cell form witch we extract the surroundings
        :return: list of surroundings cells
        '''
        out=[]
        out.append(( 'N',self.matrix[pos[0]-1][pos[1]]))
        out.append(( 'S',self.matrix[pos[0]+1][pos[1]]))
        out.append(( 'W',self.matrix[pos[0]][pos[1]-1]))
        out.append(( 'E',self.matrix[pos[0]][pos[1]+1]))
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
        self.pos = pos
        self.width,self.height=5,5
        self.map = [ [0 for i in range(self.width)] for j in range(self.height)]
        self.myworld =world

    def getPosition(self):
        return self.pos

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
        """
        build an internal model of the world given current sensors values
        :param sensors:
        :return: nothing,only internal data
        """
        # for s in sensors:
        #     if s[1]=='#':
        #         if   s[0]=='N': self.map[1][2]='#'
        #         elif s[0]=='S': self.map[3][2]='#'
        #         elif s[0]=='W': self.map[2][1]='#'
        #         else: self.map[2][3]='#'

        for s in sensors:
            if   s[0]=='N': self.map[1][2]=s[1]
            elif s[0]=='S': self.map[3][2]=s[1]
            elif s[0]=='W': self.map[2][1]=s[1]
            else: self.map[2][3]=s[1]



world = World2D(10, 10)
world.worldPrint()
world.makeRobots()
world.printRobots()
print( world.getAround((5,4)))
print(world.matrix[5][4])




