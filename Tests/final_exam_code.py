#############################################

# FINAL EXAM CODE

############################################

# a solution

import random
# helper function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std  
  
def guessfood_sim(num_trials, probs, cost, get):
    """
    num_trials: integer, number of trials to run
    probs: list of probabilities of guessing correctly for 
           the ith food, in each trial
    cost: float, how much to pay for each food guess
    get: float, how much you get for a correct guess
    
    Runs a Monte Carlo simulation, 'num_trials' times. In each trial 
    you guess what each food is, the ith food has 'prob[i]' probability 
    to get it right. For every food you guess, you pay 'cost' dollars.
    If you guess correctly, you get 'get' dollars. 
    
    Returns: a tuple of the mean and standard deviation over 
    'num_trials' trials of the net money earned 
    when making len(probs) guesses
    """
    res = []
    for _ in range(num_trials):
        money = 0
        for i in range(len(probs)):
            money-=cost
            if random.random()<=probs[i]:
                money+=get
        res.append(money)
    m, std = getMeanAndStd(res)
    return (m, std)


# ----------------- ----------------------- # 

# another solution
import random, pylab

# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    pylab.hist(values, bins = numBins)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    if title != None:
        pylab.title(title)
    pylab.show()
       
# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated to 3 decimal places
    """
    longest_runs = []
    for i in range(numTrials):
        rolls = [die.roll() for j in range(numRolls)]
        size = 1
        max_size = 0
        for i in range(len(rolls)-1):
            if rolls[i+1] == rolls[i]:
                size += 1
            else: 
                size = 1
            if max_size < size:
                max_size = size
        if max_size > 0:
            longest_runs.append(max_size)
        else:
            longest_runs.append(1)
    makeHistogram(longest_runs, numBins = 10, xLabel = 'Length of longest run', yLabel = 'frequency', title = 'Histogram of longest runs')
    return sum(longest_runs)/len(longest_runs)
        
    
# One test case
# print(getAverage(Die([1,2,3,4,5,6,6,6,7]), 500, 10000))
# print(getAverage(Die([1,2,3,4,5,6]), 50, 1000))
# print(getAverage(Die([1,2,3,4,5,6,6,6,7]), 1, 1000))          
        
# -------------------- ------------------------------------

import itertools
import numpy as np


# yet another problem
def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int
 
    Returns result, a numpy.array of length len(choices) 
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total, 
    pick the one that gives sum(result*choices) closest 
    to total without going over.
    """
    pset = []
    for i in itertools.product([1,0], repeat = len(choices)):
        pset.append(np.array(i))
    filter_set_eq = []
    filter_set_less = []
    for j in pset:
        if sum(j*choices) == total:
            filter_set_eq.append(j)
        elif sum(j*choices) < total:
            filter_set_less.append(j)
    if len(filter_set_eq) > 0:
        minidx = min(enumerate(filter_set_eq), key=lambda x:sum(x[1]))[1]
        return minidx
    else:
        minidx = max(enumerate(filter_set_less), key = lambda x:sum(x[1]))[1]
        return minidx

# ----------------------------------- --------------------------------------------

# last problem

import pylab
import random

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.
    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.
    The global variable CURRENTRABBITPOP is modified by this procedure.
    For each rabbit, based on the probabilities in the problem set write-up, 
    a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP
    for _ in range(CURRENTRABBITPOP):
        if random.random()<=(1 -(CURRENTRABBITPOP/MAXRABBITPOP)):
            CURRENTRABBITPOP += 1
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.
    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
    and both may be modified by this procedure.
    Each fox, based on the probabilities in the problem statement, may eat 
    one rabbit (but only if there are more than 10 rabbits).
    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.
    If it does not eat a rabbit, then with a 1/10 prob it dies.
    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP
    for _ in range(CURRENTFOXPOP):
        if CURRENTRABBITPOP > 10:
            if random.random()<=(CURRENTRABBITPOP/MAXRABBITPOP):
                CURRENTRABBITPOP -= 1
                # fox ke balle balle
                if random.random()<=(1/3):
                    CURRENTFOXPOP += 1
        else:
            # fox got rekt
            if random.random()<=0.9:
                CURRENTFOXPOP -= 1
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.
    Returns a tuple of two lists: (rabbit_populations, fox_populations)
    where rabbit_populations is a record of the rabbit population at the 
    END of each time step, and fox_populations is a record of the fox population
    at the END of each time step.
    Both lists should be `numSteps` items long.
    """
    rabbits, foxes = [], []
    for _ in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbits.append(CURRENTRABBITPOP)
        foxes.append(CURRENTFOXPOP)
    return rabbits, foxes

print(runSimulation(200))

# Plotting for Problem 8 Part B
def plotSimulation(numSteps):
    rabbits, foxes = [], []
    for _ in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbits.append(CURRENTRABBITPOP)
        foxes.append(CURRENTFOXPOP)
    pylab.plot(range(numSteps), rabbits, label = 'Rabbits')
    rabbit_coeff = pylab.polyfit(range(numSteps), rabbits, 2)
    pylab.plot(pylab.polyval(rabbit_coeff, range(numSteps)))
    pylab.plot(range(numSteps), foxes, label = 'Foxes')
    fox_coeff = pylab.polyfit(range(numSteps), foxes, 2)
    pylab.plot(pylab.polyval(fox_coeff, range(numSteps)))
    pylab.show()
    
plotSimulation(200)