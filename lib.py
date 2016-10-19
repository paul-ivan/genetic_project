import  math, random, time
import vrep

def getPosition(roboth):
    ret, robotPos = vrep.simxGetObjectPosition(0, roboth, -1, vrep.simx_opmode_streaming)           
    return robotPos

def setPosition(roboth, pos):
    vrep.simxSetObjectPosition(0, roboth, -1,pos,  vrep.simx_opmode_streaming)           

def setRotation(handle, angle):
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
    vrep.simxStopSimulation(0, vrep.simx_opmode_oneshot)
    
def animate(robot):
    pass

def getHandle(name):
    ret, item = vrep.simxGetObjectHandle(0, name, vrep.simx_opmode_oneshot_wait)

    if ret < 0:
        raise Exception("cant retrive item" + str(name))
    return item

def copyRobot(id_robot, num):
    ret, item = vrep.simxCopyPasteObjects(0, id_robot, vrep.simx_opmode_oneshot_wait)

    return item[0], wrist, elbow, shoulder
