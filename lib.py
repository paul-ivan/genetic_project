import vrep, math, random, time

blocking = vrep.simx_opmode_blocking
one_shot = vrep.simx_opmode_one_shot
wait = vrep.simx_opmode_one_shot_wait
streaming = vrep.simx_opmode_streaming

def setRotation(handle, angle):
    pass

def getRotation(handle):
    pass

def connect():
    idc = vrep.simxStart('127.0.0.1', 19997, True, True, 5000, 5)  
    if (idc < 0):
        raise Exception("Fail to connect")
    print("connected")

def startSimulation():
    if vrep.simxStartSimulation(0, one_shot) < 0:
        raise Exception("cant start simumation")

def stopSimulation():
    vrep.simxStopSimulation(0, one_shot)
    
def animate(robot):
    pass

def getHandle(name):
    ret, item = vrep.simxGetObjectHandle(0, name, blocking)

    if ret < 0:
        raise Exception("cant retrive item" + str(name))
    return item

def copyRobot(id_robot):
    ret, item = vrep.simxCopyPasteObjects(0, id_robot, blocking)
