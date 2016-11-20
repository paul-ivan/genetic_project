#!/usr/bin/python3 -i

import vrep, math, random, time, copy, lib as ml
from deap import base, creator, tools
import vector as vv
from decimal import Decimal

NB_GENERATIONS = 100000
NB_ROBOTS = 10
NB_GENES = 20

#Initialisation
vrep.simxFinish(-1)
ml.connect()
ml.stopSimulation()
ml.loadScene()

random.seed()
wrist = ml.getHandle("WristMotor")
elbow = ml.getHandle("ElbowMotor")
shoulder = ml.getHandle("ShoulderMotor")
robot = ml.getHandle("2W1A")


rb_cur = 0
rbtLst = [[robot, wrist, elbow, shoulder]]
initPos = ml.getPosition(robot)
ml.setPosition(robot, [initPos[0], initPos[1] -  1.5, initPos[2]])
initPos = ml.getPosition(robot)
print(initPos)
for i in range(1, NB_ROBOTS):
    new_rb = ml.copyRobot(robot, i - 1)
    rbtLst.append(new_rb)
    pos = [initPos[0], 0.4 + initPos[1] + (0.4 *  (i - 1)), initPos[2]]
    ml.setPosition(new_rb[0], pos)
print("starting")
print ("robot %s wrist %s elbow %s shoulder %s" % (robot, wrist, elbow, shoulder))



def my_cross(r):
    pass

def my_mutate(ind):
    print ("MUTATING")
    for i, angle in enumerate(ind):
        if random.random() <= 0.1:
            ind[i] = getRand()
    return ind

def l_gen():
    print("CREATING NEW gen §§!!!!!!§§§")
    return getRand()


def evalInd(ar):
    global rb_cur

    ml.startSimulation()
    res  = [-1] * len(ar)
    follow = False
    k = 0
    pos = []
    iters = 0;
    b = True
    while b == True and iters < 10:
        b = False
        for i in range(0, NB_GENES, 2):
            for ROBOT_INDEX in range(0, len(ar)):
                r = rbtLst[ROBOT_INDEX]
                if (i == 0):
                    res[ROBOT_INDEX] = ml.getPosition(r[0])[0]
                w = r[1]
                e = r[2]
                ml.move_motor(w, ar[ROBOT_INDEX][i])
                ml.move_motor(e, ar[ROBOT_INDEX][i + 1])

                if (i == NB_GENES - 2):
                    end_pos = ml.getPosition(r[0])[0]
                    if res[ROBOT_INDEX] >  end_pos:
                        b = True
                    res[ROBOT_INDEX] = end_pos
            time.sleep(0.5)
        iters += 1
    print("xs= " + str(res))
    ml.stopSimulation()
    return res

creator.create("FitnessMax", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness = creator.FitnessMax)

toolbox = base.Toolbox()
toolbox.register("genrator_gene", lambda: l_gen())
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.genrator_gene, NB_GENES) 
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("evaluate", evalInd)
toolbox.register("mate", tools.cxTwoPoint)
#toolbox.register("mutate", tools.mutUniformInt, low = 0, up = 300, indpb = 0.50)

toolbox.register("mutate", my_mutate)
toolbox.register("select", tools.selTournament, tournsize = 3)


def getRand(step = 10):
    lst = []
    for i in range (0, 300, step):
        lst.append(i)
    return random.choice(lst)


# Begin the evolution

pop = toolbox.population(n = NB_ROBOTS)
fits = list(toolbox.evaluate(pop))

for ind, fit in zip(pop, fits):
    ind.fitness.fit = fit
MUTPB =  0.6
CXPB = 0.4

for g in range(NB_GENERATIONS):
    print("-- Generation %i --" % g)
    offspring = toolbox.select(pop, len(pop))
    offspring = list(map(toolbox.clone, offspring))
    print ([str(f) for f in offspring] )
    for child1, child2 in zip(offspring[::2], offspring[1::2]):
        if random.random() < CXPB:
            toolbox.mate(child1, child2)
            del child1.fitness.values
            del child2.fitness.values
    for mutant in offspring:
        if random.random() < MUTPB:
            toolbox.mutate(mutant)
            del mutant.fitness.values
    invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
    fitnesses =  toolbox.evaluate(invalid_ind)
    for ind, fit in zip(invalid_ind, fitnesses):
        ind.fitness.values = fit,
    pop[:] = offspring
    fits = [ind.fitness.values[0] for ind in pop]
    length = len(pop)
    mean = sum(fits) / length
    sum2 = sum(x*x for x in fits)
    std = abs(sum2 / length - mean**2)**0.5
    print("  Min %s" % min(fits))
    print("  Max %s" % max(fits))
    print("  Avg %s" % mean)
    print("  Std %s" % std)
print("-- End of (successful) evolution --")
best_ind = tools.selBest(pop, 1)[0]
print("Best individual is %s, %s" % (best_ind, best_ind.fitness.values))
