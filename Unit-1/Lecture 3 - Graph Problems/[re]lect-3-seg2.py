# reimplementation of lecture3-segment2.py for better understanding.


class Node(object):
    def __init__(self, name):
        """Assuming name is a string"""
        self.name = name

    def getName(self):
        return self.name

    def __str__(self):
        return self.name


class Edge(object):
    def __init__(self, src, dest):
        """Assuming src and dest are nodes"""
        self.src = src
        self.dest = dest

    def getSource(self):
        return self.src

    def getDest(self):
        return self.dest

    def __str__(self):
        return self.src.getName() + ' --> ' + self.dest.getName()


class DirectedGraph(object):
    """
    menial implementation of an adjacency list | dict mapping class Node to class Edge
    edges are a dict mapping each node to a list of child nodes
    """

    def __init__(self):
        self.edges = {}

    def addNode(self, node):
        if node in self.edges:
            raise ValueError('Node already present.')
        else:
            self.edges[node] = []

    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDest()
        if not (src in self.edges and dest in self.edges):
            raise ValueError('Node not present in graph.')
        else:
            self.edges[src].append(dest)

    def childrenOf(self, node):
        return self.edges[node]

    def hasNode(self, node):
        return node in self.edges

    def getNode(self, name):
        for node in self.edges:
            if node.getName() == name:
                return node
        raise NameError(name)

    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result = result + src.getName() + ' --> ' + dest.getName() + '\n'
        return result[:-1]  # omit final \n


class Graph(DirectedGraph):
    # overwriting addEdge of DirectedGraph
    def addEdge(self, edge):
        DirectedGraph.addEdge(self, edge)
        rev = Edge(edge.getDest(), edge.getSource())
        DirectedGraph.addEdge(self, rev)


'''
Adjacency list for airline problem:
Node : Children

Boston : Providence, NY
Providence : Boston, NY
NY : Chicago
Chicago : Denver, Phoenix
Denver : Phoenix, NY
LA : Boston
'''


def buildCityGraph(graphType):
    g = graphType()
    for name in ('Boston', 'Providence', 'New York', 'Chicago', 'Denver', 'Phoenix', 'Los Angeles'):  # Create 7 nodes
        g.addNode(Node(name))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('Providence')))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('Boston')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('New York'), g.getNode('Chicago')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Denver')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Los Angeles'), g.getNode('Boston')))
    return g


# print(buildCityGraph(Graph))  # round trips visible
# print()
# print(buildCityGraph(DirectedGraph))  # only one to one

########################################################################

# Exercise 2

# Exercise 2
# 10/10 points (graded)
# Consider our representation of permutations of students in a line from Exercise 1. (The teacher only swaps the positions of two
# students that are next to each other in line.) Let's consider a line of three students, Alice, Bob, and Carol (denoted A, B, and C).
# Using the Graph class created in the lecture, we can create a graph with the design chosen in Exercise 1: vertices represent
# permutations of the students in line; edges connect two permutations if one can be made into the other by swapping two adjacent
# students.

# We construct our graph by first adding the following nodes:

nodes = []
nodes.append(Node("ABC"))  # nodes[0]
nodes.append(Node("ACB"))  # nodes[1]
nodes.append(Node("BAC"))  # nodes[2]
nodes.append(Node("BCA"))  # nodes[3]
nodes.append(Node("CAB"))  # nodes[4]
nodes.append(Node("CBA"))  # nodes[5]

g = Graph()
for n in nodes:
    g.addNode(n)
# Add the appropriate edges to the graph.
g.addEdge(Edge(g.getNode('ABC'), g.getNode('ACB')))
g.addEdge(Edge(g.getNode('ABC'), g.getNode('BAC')))
g.addEdge(Edge(g.getNode('ACB'), g.getNode('CAB')))
g.addEdge(Edge(g.getNode('BAC'), g.getNode('BCA')))
g.addEdge(Edge(g.getNode('BCA'), g.getNode('CBA')))
g.addEdge(Edge(g.getNode('CAB'), g.getNode('CBA')))


print(g)

# 20/20 (on second try though :-(
