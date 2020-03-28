# reimplementation of lecture2-segment3.py for better understanding.

'''
Question : so when exactly should I use DP
Answer : According to it's creator, it's useful when a program has
- optimal substructure
A problem has optimal substructure if a globally optimal solution can be
found by combining optimal solutions to local subproblems.
- overlapping subproblems
A problem has overlapping subproblems if an optimal solution involves solv-
ing the same problem multiple times.
'''


class Food(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w

    def getValue(self):
        return self.value

    def getCost(self):
        return self.calories

    def density(self):
        return self.getValue() / self.getCost()

    def __str__(self):
        return self.name + ': <' + str(self.value) \
               + ', ' + str(self.calories) + '>'


def buildMenu(names, values, calories):
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i],
                         calories[i]))
    return menu


def maxVal(toConsider, avail):
    """Assumes toConsider a list of items, avail a weight
       Returns a tuple of the total weight of a solution to the
         0/1 knapsack problem and the items of that solution"""
    if toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getCost() > avail:
        # Explore right branch only
        result = maxVal(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]
        # Explore left branch
        withVal, withToTake = maxVal(toConsider[1:],
                                     avail - nextItem.getCost())
        withVal += nextItem.getValue()
        # Explore right branch
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)
        # Choose better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    return result


import random


def buildLargeMenu(numItems, maxVal, maxCost):
    items = []
    for i in range(numItems):
        items.append(Food(str(i),
                          random.randint(1, maxVal),
                          random.randint(1, maxCost)))
    return items

def fastMaxVal(toConsider, avail, mem=None):
    '''
    key of mem is a tuple
    (length of items left to be considered, available weight)
    Returns a tuple of the total value of a solution to the
    0/1 knapsack problem and the subjects of that solution"""
    '''
    if mem is None:
        mem = {}
    # check if items with the current weight left already memoized
    if (len(toConsider), avail) in mem:
        # result already stored data
        result = mem[(len(toConsider), avail)]
    elif toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getCost() > avail:
        # go down right branch
        result = fastMaxVal(toConsider[1:], avail, mem)
    else:
        nextItem = toConsider[0]
        # explore right branch
        withVal, withToTake = fastMaxVal(toConsider[1:],
                                         avail - nextItem.getCost(), mem)
        withVal += nextItem.getValue()
        # explore left branch
        withoutVal, withoutToTake = fastMaxVal(toConsider[1:],
                                               avail, mem)
        # choose better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem, ))
        else:
            result = (withVal, withoutToTake + (nextItem, ))
    # memoization
    mem[(len(toConsider), avail)] = result
    return result


def testMaxVal(foods, maxUnits, algorithm, printItems=True):
    print('Menu contains', len(foods), 'items')
    print('Use search tree to allocate', maxUnits,
          'calories')
    val, taken = algorithm(foods, maxUnits)
    if printItems:
        print('Total value of items taken =', val)
        for item in taken:
            print('   ', item)

# building a large menu with > 40 items is very inefficient
# gotta resort to DP for this task
for numItems in (5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 150, 625):
    items = buildLargeMenu(numItems, 90, 250)
    testMaxVal(items, 750, fastMaxVal, False)

# doing for numItems = 1024 gives us an error of reaching max recursive depth.
# which is set to 1000, btw we can change it with sys.setrecursionlimit(lim)



