#!/usr/bin/python3 -i

import math, random, time, copy, lib as ml
from deap import base, creator, tools
from decimal import Decimal

NB_GENES = 3
NB_ROBOTS = 5
NB_GENERATIONS = 5

def getRandLst(step = 20):
    return getRand(step)

def l_gen():
    print("CREATING NEW gen §§!!!!!!§§§")
    return getRand()

def evalPop(res):
    print("evaluating")
    r = []
    for i in range(0, len(res)):
        print(res[i])
        r.append(random.randint(0, 10))
    print (r)
    print("MAX =" + str(min(r)))
    return r;

def my_mutate(ind):
    print("----MUTATING----")
    for angle in ind:
        if random.random() < 0.5 :
            angle = getRand()
    return ind

creator.create("FitnessMax", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness = creator.FitnessMax)

toolbox = base.Toolbox()
toolbox.register("genrator_gene", lambda: l_gen())
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.genrator_gene, NB_GENES) 
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("evaluate", evalPop)
toolbox.register("mate", tools.cxTwoPoint)
#toolbox.register("mutate", tools.mutUniformInt, low = 0, up = 300, indpb = 0.50)

toolbox.register("mutate", my_mutate)
toolbox.register("select", tools.selTournament, tournsize = 3)


def getRand(step = 10):
    lst = []
    for i in range (0, 300, step):
        lst.append(i)
    return random.choice(lst)

pop = toolbox.population(n = NB_ROBOTS)
fits = toolbox.evaluate(pop)
print("FITS" + str(fits))
print("POPS" + str(pop))
for ind, fit in zip(pop, fits):
    ind.fitness.fit = fit
MUTPB =  0.7
CXPB = 0.4

# Begin the evolution

for g in range(NB_GENERATIONS):
    print("-- Generation %i --" % g)
    offspring = toolbox.select(pop, len(pop))
    offspring = list(map(toolbox.clone, offspring))
    #print ([str(f) for f in offspring] )

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
    fitnesses = toolbox.evaluate(invalid_ind)
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
