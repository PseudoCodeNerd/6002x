# reimplementing lect6-segment1.py for better understanding

"""
Structure of Simulation
- Simulate one walk of k steps
- Simulate n such walks
- Prepare report (average distance from origin)
"""

import random
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


class ColdDrunk(Drunk):
    """
    avoids north of Maine state where it is cold.
    """
    def takeStep(self):
        stepPoss = [(0, 0.8), (0, -1.2), (1, 0), (-1, 0)]
        return random.choice(stepPoss)


def simWalkAll(walk_lengths, num_trials, d_types):
    for d_type in d_types:
        test(walk_lengths, num_trials, d_type)


random.seed(0)

simWalkAll((10, 100, 1000, 10000), 1000, (UsualDrunk, ColdDrunk))
