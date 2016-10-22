import  math, random, time
import vrep

def loadScene():
    vrep.simxCloseScene(0, vrep.simx_opmode_oneshot)
    print ("loading scene")
    if vrep.simxLoadScene(0, "/home/tutu/projects/ia/2wheel1arm/test/2w1a.ttt", 0, vrep.simx_opmode_blocking) < 0:
        raise Exception("cannot load scene")


def getPosition(roboth):
    ret, robotPos = vrep.simxGetObjectPosition(0, roboth, -1, vrep.simx_opmode_blocking)           
    return robotPos

def setPosition(roboth, pos):
    vrep.simxSetObjectPosition(0, roboth, -1,pos,  vrep.simx_opmode_streaming)           

def setRotation(handle, angle):
    pass

def connect():
    idc = vrep.simxStart('127.0.0.1', 19997, True, True, 5000, 5)  
    print("client is %s" %idc)
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
    ret, item = vrep.simxGetObjectHandle(0, name, vrep.simx_opmode_blocking)

    if ret < 0:
        raise Exception("cant retrive item" + str(name))
    return item

def copyRobot(id_robot, num):
    ret, item = vrep.simxCopyPasteObjects(0, [id_robot], vrep.simx_opmode_blocking)
    print(item)
    wrist = getHandle("WristMotor#" + str(num)) 
    elbow = getHandle("ElbowMotor#" + str(num))
    shoulder = getHandle("ShoulderMotor#" + str(num))

    return item[0], wrist, elbow, shoulder


