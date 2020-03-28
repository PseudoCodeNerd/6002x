# reimplementation of lecture2-segment2.py for better understanding.

class Food(object):
    def __init__(self, v, n, w):
        self.name = n
        self.value = v
        self.calories = w
    def getValue(self):
        return self.value
    def getName(self):
        return self.name
    def getCost(self):
        return self.calories
    def ratio(self):
        return self.getValue()/self.getCost()
    def __str__(self):
        return self.name + ' : (' + str(self.value) + ', ' + str(self.calories) + ')'

def menuBuilder(names, values, calories):
    '''
    names, values ans weights are lists of same length
    :param name:
    :param values:
    :param weights:
    :return: list of foods
    '''
    menu = []
    for i in range(len(values)):
        menu.append(Food(values[i], names[i], calories[i]))
    return menu

def maxVal(toConsider, avail):
    '''
    record best soln found so far, doesn't **build** a decision tree
    :param toConsider: items yet to be considered in nodes
    :param avail: the amount of space still available
    :return: tuple of the total value of a solution to the
            0/1 knapsack problem and the items of that solution
    '''
    if toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getCost() > avail:
        #Explore right branch only
        result = maxVal(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]
        #Explore left branch
        withVal, withToTake = maxVal(toConsider[1:],
                                     avail - nextItem.getCost())
        withVal += nextItem.getValue()
        #Explore right branch
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)
        #Choose better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    return result

def testMaxVal(foods, maxUnits, printItems = True):
    print('Use search tree to allocate', maxUnits,
          'calories')
    val, taken = maxVal(foods, maxUnits)
    print('Total value of items taken =', val, '\n')
    if printItems:
        for item in taken:
            print('   ', item)

# building large menus
import random

def buildLargeMenu(numItems, maxVal, maxCost):
    items = []
    for i in range(numItems):
        items.append(Food(random.randint(1, maxVal), str(i),
                                    random.randint(1, maxCost)))
    return items

# building a large menu with > 40 items is very ineffcient
# gotta resort to DP for this task
for numItems in (5, 10, 15, 20, 25, 30, 35, 40, 45):
    print('Try a menu with', numItems, 'items')
    items = buildLargeMenu(numItems, 90, 250)
    testMaxVal(items, 750, False)

# need for dynamic programming understood via comparision b/w
# normie and dank ways to compute nth term of a fibonaccci series

def normie_fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return normie_fibonacci(n - 1) + normie_fibonacci(n - 2)


def dank_fibonacci(n, mem=None):
    if mem is None:
        mem = {}
    if n == 0 or n == 1:
        return 1
    try:
        return mem[n]
    except KeyError:
        result = dank_fibonacci(n - 1, mem) + dank_fibonacci(n - 2, mem)
        mem[n] = result
        return result


print(normie_fibonacci(15))
print('\n')
print(dank_fibonacci(15))

# change dank to normie to see how the time to calculate via normie increases exponentially
for i in range(120):
    print('fib(' + str(i) + ') =', dank_fibonacci(i))

# thus DP is enormous win for fibonacci.


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