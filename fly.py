import sys
sys.path.append('/usr/local/lib/python3.9/site-packages')
import getch
from easytello import tello
drone = tello.Tello()
t = True
x = int(input("speed?>"))
y = int(input("turn speed>"))
drone.takeoff()
while t == True:
    key = getch.getch()
    if key=="w":
        drone.forward(x)
    elif key=="a":
        drone.left(x)
    elif key=="s":
        drone.back(x)
    elif key=="d":
        drone.right(x)
    elif key=="i":
        drone.up(x)
    elif key=="j":
        drone.ccw(y)
    elif key=="k":
        drone.down(x)
    elif key=="l":
        drone.cw(y)
    elif key=="m":
        drone.land()
    elif key=="n":
        x = int(input("new speed?>"))
    elif key=="b":
        y = int(input("new turn>"))
    elif key=="h":
        drone.takeoff()