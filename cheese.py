from easytello import tello 
drone=tello.Tello()
drone.takeoff()
y = True
for i in range(3):
    y = True
    while y == True:
        tof = int(drone.get_tof())/10
        if tof > 45:
            if tof < 75:
                drone.forward(80)
                y = False
            elif tof > 75:
                drone.down(20)
        elif tof < 45:
            drone.up(20)
        else:
            drone.forward(80)
            y = False




























drone.land()
