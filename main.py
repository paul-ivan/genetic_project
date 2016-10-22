#!/usr/bin/python3 -i

import vrep, math, random, time, copy, lib as ml

NB_GENERATIONS = 300
NB_ROBOTS = 2


#Initialisation

vrep.simxFinish(-1)
ml.connect()
ml.loadScene()
wrist = ml.getHandle("WristMotor")
elbow = ml.getHandle("ElbowMotor")
shoulder = ml.getHandle("Shoulder")
robot = ml.getHandle("2W1A")

rbtLst = [[robot, wrist, elbow, shoulder]]
initPos = ml.getPosition(robot)
print(initPos)

for i in range(0, NB_ROBOTS):
    new_rb = ml.copyRobot(robot, i)
    rbtLst.append(new_rb)
    pos = [initPos[0], 0.5 + initPos[1] + (0.5 * i), initPos[2]]
    ml.setPosition(new_rb[0], pos)


print("starting")
print ("robot %s wrist %s elbow %s shoulder %s" % (robot, wrist, elbow, shoulder))
