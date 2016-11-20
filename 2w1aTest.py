# File created by Thibaut Royer, Epitech school
# thibaut1.royer@epitech.eu
# It intends to be an example program for the "Two wheels, one arm" educative project.

import vrep
import math
import random
import time

print ('Start')

# Close eventual old connections
vrep.simxFinish(-1)
# Connect to V-REP remote server
clientID = vrep.simxStart('127.0.0.1', 19997, True, True, 5000, 5)

if clientID != -1:
    print ('Connected to remote API server')

    # Communication operating mode with the remote API : wait for its answer before continuing (blocking mode)
    # http://www.coppeliarobotics.com/helpFiles/en/remoteApiConstants.htm
    opmode = vrep.simx_opmode_oneshot_wait

    # Try to retrieve motors and robot handlers
    # http://www.coppeliarobotics.com/helpFiles/en/remoteApiFunctionsPython.htm#simxGetObjectHandle
    ret1, wristHandle = vrep.simxGetObjectHandle(clientID, "WristMotor", opmode)
    ret2, elbowHandle = vrep.simxGetObjectHandle(clientID, "ElbowMotor", opmode)
    ret3, shoulderHandle = vrep.simxGetObjectHandle(clientID, "ShoulderMotor", opmode)
    ret4, robotHandle = vrep.simxGetObjectHandle(clientID, "2W1A", opmode)

    # If handlers are OK, execute three random simulations
    if ret1 == 0 and ret2 == 0 and ret3 == 0:
        random.seed()
        for i in range(0, 3):
            # Start the simulation
            # http://www.coppeliarobotics.com/helpFiles/en/remoteApiFunctionsPython.htm#simxStartSimulation
            vrep.simxStartSimulation(clientID, opmode)
            print ("----- Simulation started -----")

            for j in range(0, 5):
                # Generating random positions for the motors
                awrist = random.randint(0, 300)
                aelbow = random.randint(0, 300)
                ashoulder = random.randint(0, 300)
                
                vrep.simxSetJointTargetPosition(clientID, wristHandle, math.radians(awrist), opmode)
                vrep.simxSetJointTargetPosition(clientID, elbowHandle, math.radians(aelbow), opmode)
                vrep.simxSetJointTargetPosition(clientID, shoulderHandle, math.radians(ashoulder), opmode)

                # Wait in order to let the motors finish their movements
                # Tip: there must be a more efficient way to do it...
                time.sleep(0.5)

            vrep.simxStopSimulation(clientID, opmode)
            time.sleep(1)

    # Close the connection to V-REP remote server
    # http://www.coppeliarobotics.com/helpFiles/en/remoteApiFunctionsPython.htm#simxFinish
    vrep.simxFinish(clientID)
else:
    print ('Failed connecting to remote API server')
print ('End')
