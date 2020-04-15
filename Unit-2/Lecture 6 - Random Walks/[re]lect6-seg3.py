# reimplementing lect6-segment1.py for better understanding

"""
Structure of Simulation
- Simulate one walk of k steps
- Simulate n such walks
- Prepare report (average distance from origin)
"""

import random
import matplotlib.pylab as pylab

random.seed(0)


class Location(object):

    def __init__(self, x, y):
        """
        x and y are floats
        """
        self.x = x
        self.y = y

    def move(self, delX, delY):
        """
        delX and delY are numbers/floats
        """
        return Location(self.x + delX, self.y + delY)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distFrom(self, other):
        xDist = self.x - other.x
        yDist = self.y - other.y
        return (xDist ** 2 + yDist ** 2) ** 0.5

    def __str__(self):
        return '( ' + str(self.x) + ', ' + str(self.y) + ' )'


class Drunk(object):

    def __int__(self, name=None):
        self.name = name

    def __str__(self):
        if self != None:
            return self.name
        return 'Unknown'


class UsualDrunk(Drunk):

    def takeStep(self):
        stepPoss = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        return random.choice(stepPoss)


class ColdDrunk(Drunk):
    """
    avoids north of Maine state where it is cold aka heat seaking drunk.
    """

    def takeStep(self):
        stepPoss = [(0, 0.8), (0, -1.2), (1, 0), (-1, 0)]
        return random.choice(stepPoss)


class Field(object):

    def __init__(self):
        self.drunks = {}

    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Drunk already exists.')
        else:
            self.drunks[drunk] = loc

    def moveDrunk(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field.')
        xDist, yDist = drunk.takeStep()
        currLocation = self.drunks[drunk]
        # move to a new location
        self.drunks[drunk] = currLocation.move(xDist, yDist)

    def getDrunkLoc(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field.')
        return self.drunks[drunk]


def walk(F, D, num_steps):
    """
    simulate one walk of D drunk in F field of num_steps steps.
    """
    init = F.getDrunkLoc(D)
    for _ in range(num_steps):
        F.moveDrunk(D)
    return init.distFrom(F.getDrunkLoc(D))


def simWalk(num_steps, num_trials, d_type):
    """
    simulates num_trials number of walks each with num_steps number of
    steps with a d_type drunk object class.
    """
    drunkard = d_type()
    origin = Location(0, 0)
    distances = []
    for _ in range(num_trials):
        F = Field()
        F.addDrunk(drunkard, origin)
        distances.append(round(walk(F, drunkard, num_steps)))
    return distances


def test(walk_length, num_trials, d_type):
    """
    for each number of steps in walk_length, simWalk with num_trials
    number of trials of each walk.
    """
    for num_steps in walk_length:
        distance = simWalk(num_steps, num_trials, d_type)
        print(d_type.__name__, 'random walk of', num_steps, 'steps.')
        print('Stats for distance from the origin.')
        print('Mean --> ', round(sum(distance) / len(distance), 4))
        print('Max --> ', max(distance), '\t Min --> ', min(distance), '\n')


# test((10, 100, 1000, 10000), 100, UsualDrunk)
# test((10, 100, 1000, 10000), 1000, UsualDrunk)


def simWalkAll(walk_lengths, num_trials, d_types):
    for d_type in d_types:
        test(walk_lengths, num_trials, d_type)


random.seed(0)

# simWalkAll((10, 100, 1000, 10000), 1000, (UsualDrunk, ColdDrunk))

# Plotting simulation.


# set line width
pylab.rcParams['lines.linewidth'] = 4
# set font size for titles
pylab.rcParams['axes.titlesize'] = 20
# set font size for labels on axes
pylab.rcParams['axes.labelsize'] = 20
# set size of numbers on x-axis
pylab.rcParams['xtick.labelsize'] = 16
# set size of numbers on y-axis
pylab.rcParams['ytick.labelsize'] = 16
# set size of ticks on x-axis
pylab.rcParams['xtick.major.size'] = 7
# set size of ticks on y-axisz
pylab.rcParams['ytick.major.size'] = 7
# set size of markers, e.g., circles representing points
# set numpoints for legend
pylab.rcParams['legend.numpoints'] = 1


class styleIter(object):

    def __init__(self, styles):
        self.index = 0
        self.styles = styles

    def next_style(self):
        result = self.styles[self.index]
        # if reached end of syle_lis, go back to first elem
        if self.index == len(self.styles) - 1:
            self.index = 0
        else:
            self.index += 1
        return result


def simDrunk(walk_length, num_trials, d_type):
    mean_distances = []
    for num_steps in walk_length:
        print('Begin simulation of ', num_steps, 'steps.')
        trials = simWalk(num_steps, num_trials, d_type)
        mean_distances.append(sum(trials) / len(trials))
    return mean_distances


def simWalkAll(walk_length, num_trials, d_types):
    style_choice = styleIter(('m-', 'b--', 'g-.'))
    for d_type in d_types:
        curStyle = style_choice.next_style()
        print('Starting simulation of ', d_type.__name__, '\n')
        mean_values = simDrunk(walk_length, num_trials, d_type)
        pylab.plot(walk_length, mean_values, curStyle, label=d_type.__name__)
    pylab.title('Mean distance from the origin (' + str(num_trials) + ') trials.')
    pylab.xlabel('Number of Steps')
    pylab.ylabel('Distance from Origin')
    pylab.legend(loc='best')


# random.seed(0)
# walk_lengths = (10, 100, 1000, 10000)
# simWalkAll(walk_lengths, 1000, (UsualDrunk, ColdDrunk))
# pylab.show()


# To better understand why heat seeking drunk is moving fast at a linear rate.
# We'll try to produce a plot with points telling us where a particular walk ends.

def getFinLocs(num_steps, num_trials, d_type):
    fin_locns = []
    drunkard = d_type()
    for _ in range(num_trials):
        F = Field()
        F.addDrunk(drunkard, Location(0, 0))
        for _ in range(num_steps):
            F.moveDrunk(drunkard)
        fin_locns.append(F.getDrunkLoc(drunkard))
    return fin_locns


def plotFinLocs(num_steps, num_trials, d_types):
    style_choice = styleIter(('k+', 'r^', 'mo'))
    for d_type in d_types:
        print('Starting simulation of', d_type.__name__, '\n')
        fin_locns = getFinLocs(num_steps, num_trials, d_type)
        xVals, yVals = [], []
        for fin_locn in fin_locns:
            xVals.append(fin_locn.getX())
            yVals.append(fin_locn.getY())
        xVals, yVals = pylab.array(xVals), pylab.array(yVals)
        meanX = sum(abs(xVals)) / len(xVals)
        meanY = sum(abs(yVals)) / len(yVals)
        cur_style = style_choice.next_style()
        pylab.plot(xVals, yVals, cur_style,
                   label=d_type.__name__ + ' mean abs dist = <' + str(meanX) +
                         ', ' + str(meanY) + '>')
    pylab.title('Location at End of Walks ('
                + str(num_steps) + ' steps)')
    pylab.ylim(-1500, 1500)
    pylab.xlim(-1500, 1500)
    pylab.xlabel('Steps East/West of Origin')
    pylab.ylabel('Steps North/South of Origin')
    pylab.legend(loc='upper left')


# random.seed(0)
# plotFinLocs(10000, 1000, (UsualDrunk, ColdDrunk))
# pylab.show()

# Now we are in a position to explain why the plot looks like this.
# From our ColdDrunk definition our possible steps are [(0, 0.8), (0, -1.2), (1, 0), (-1, 0)]
# thus for every four steps, the cold drunk moves down once and once up. After these two moves, he is
# 0.4 units down from where he initially was. So, for every 4 steps he moves 0.4 that for every move he moves
# 0.1 step down. Hence, the angle at which the line was at in result_plot1.png.

# Now, let's change properties of the Field itself, by adding wormholes.
# This field has some coordinates if on which a drunkard lands, he is immediately teleported to another coordinate. Dope

class TeleportationField(Field):

    def __init__(self, num_holes=1000, xRange=100, yRange=100):
        Field.__init__(self)
        self.wormholes = {}
        for _ in range(num_holes):
            x = random.randint(-xRange, xRange)
            y = random.randint(-yRange, yRange)
            newX = random.randint(-xRange, xRange)
            newY = random.randint(-yRange, yRange)
            # TELEPORTATION WHEEE...
            new_locn = Location(newX, newY)
            self.wormholes[(x, y)] = new_locn

    def moveDrunk(self, drunk):
        Field.moveDrunk(self, drunk)
        x = self.drunks[drunk].getX()
        y = self.drunks[drunk].getY()
        if (x, y) in self.wormholes:
            self.drunks[drunk] = self.wormholes[(x, y)]


# Trace walk in the TeleportationField
def traceWalk(fields, numSteps):
    styleChoice = styleIter(('b+', 'r^', 'ko'))
    for field in fields:
        D = UsualDrunk()
        F = field()
        F.addDrunk(D, Location(0, 0))
        locs = []
        for s in range(numSteps):
            F.moveDrunk(D)
            locs.append(F.getDrunkLoc(D))
        xVals, yVals = [], []
        for loc in locs:
            xVals.append(loc.getX())
            yVals.append(loc.getY())
        curStyle = styleChoice.next_style()
        pylab.plot(xVals, yVals, curStyle,
                   label=field.__name__)
    pylab.title('Spots Visited on Walk ('
                + str(numSteps) + ' steps)')
    pylab.xlabel('Steps East/West of Origin')
    pylab.ylabel('Steps North/South of Origin')
    pylab.legend(loc='best')


random.seed(0)
traceWalk((Field, TeleportationField), 500)
pylab.show()
