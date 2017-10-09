from simulatore import World2D
from simulatore import Robot
from simulatore import GUI
from threading import *
import random
import time


def run(i):
    print("Starting thread %d", i)
    direction=["N","S","E","W"]
    print("Exiting thread %d", i)
    r_i=world.robotList[i]
    for k in range(8):
        r_i.move(direction[random.randint(0, 3)],world)


world=World2D(10,10)
world.makeRobots()
world.worldPrint()
g=GUI()
g.updateInterface(world)
time.sleep(5)
threads=[]

for i in range(9):
    if current_thread()==main_thread():
        t = Thread(target=run, args=(i,))
        t.start()
        threads.append(t)

for k in threads:
    k.join()

world.worldPrint()
g.updateInterface(world)
time.sleep(5)
