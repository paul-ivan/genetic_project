#!/usr/bin/python3 -i

import vrep, math, random, time, lib as ml

NB_GENERATIONS = 300



vrep.simxFinish(-1)
ml.connect()


wrist = ml.getHandle("WristMotor")
elbow = ml.getHandle("ElbowMotor")
shoulder = ml.getHandle("Shoulder")
robot = ml.getHandle("2W1A")
