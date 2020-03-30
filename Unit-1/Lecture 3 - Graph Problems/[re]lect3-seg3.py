# reimplementation of lecture3-segment.py for better understanding.


class Node(object):
    def __init__(self, name):
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


class Digraph(object):
    def __init__(self):
        self.edges = {}

    def addNode(self, node):
        if node in self.edges:
            raise KeyError('Duplicate node present already.')
        else:
            self.edges[node] = []

    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDest()
        if not (src in self.edges and dest in self.edges):
            raise KeyError('Node not present in graph.')
        else:
            self.edges[src].append(dest)

    def getNode(self, name):
        for node in self.edges:
            if node.getName() == name:
                return node
        raise NameError(name)

    def hasNode(self, node):
        return node in self.edges

    def nodeChildren(self, node):
        return self.edges[node]

    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result = result + src.getName() + ' --> ' + dest.getName() + '\n'
        return result[:-1]


class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDest(), edge.getSource())
        Digraph.addEdge(self, rev)


def buildCityGraph(graphType):
    g = graphType()
    for name in ('Boston', 'Providence', 'New York', 'Chicago',
                 'Denver', 'Phoenix', 'Los Angeles'):
        g.addNode(Node(name))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('Providence')))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('Boston')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('New York'), g.getNode('Chicago')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Denver')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Los Angeles'), g.getNode('Boston')))
    return g


# print function


def printPath(path):
    """Assuming path is a list of nodes."""
    result = ''
    for i in range(len(path)):
        result += str(path[i])
        if i != len(path) - 1:
            result += ' --> '
    return result


# Depth First Search


def dfs(graph, start, end, path, shortest, to_print):
    """
    Assumes a digraph with start and ends as nodes, return the shortest path as a
    list of nodes between them. to_print conditional decided whether to print
    explanatory stuff or not.
    """
    path = path + [start]
    if to_print:
        print('Current DFS Path : ', printPath(path))
    if start == end:
        return path
    for node in graph.nodeChildren(start):
        if node not in path:  # avoids cycling by keeping a visited nodes list
            if shortest is None or len(path) < len(shortest):
                new_path = dfs(graph, node, end, path, shortest, to_print)
                if new_path is not None:
                    shortest = new_path
        elif to_print:
            print('Node already visited. Skipping...')
    return shortest


def DFSshortestPath(graph, start, end, to_print=False):
    return dfs(graph, start, end, [], None, to_print)


def DFStestSP(source, destination):
    g = buildCityGraph(Digraph)
    sp = DFSshortestPath(g, g.getNode(source), g.getNode(destination),
                         to_print=True)
    if sp is not None:
        print('\nShortest path from', source, 'to', destination, 'is\n', printPath(sp))
    else:
        print('There is no path from', source, 'to', destination)


print('Adjacency list is as follows :\n', buildCityGraph(Digraph), '\n\n')
# testSP('Chicago', 'Boston')
DFStestSP('Boston', 'Phoenix')
print()


def bfs(graph, start, end, to_print):
    """
    Assumes a digraph with start and ends as nodes, return the shortest path as a
    list of nodes between them. to_print conditional decided whether to print
    explanatory stuff or not.
    """

    # the initial path is the starting node
    init_path = [start]
    path_queue = [init_path]
    while len(path_queue) != 0:
        # take out of the queue the first path / current path
        curr_path = path_queue.pop(0)
        if to_print:
            print('Current BFS Path : ', printPath(curr_path))
            last_node = curr_path[-1]
            if last_node == end:
                return curr_path
            # if the last node of current path isn't the end point, move on to paths
            # generated by it's children
            for node in graph.nodeChildren(last_node):
                # if the child node is not in current path, add it to curr_path
                if node not in curr_path:
                    new_path = curr_path + [node]
                    # add new possible path to path queue
                    path_queue.append(new_path)


def BFSshortestpath(graph, start, end, to_print=True):
    return bfs(graph, start, end, to_print)


def BFStestSP(source, destination):
    g = buildCityGraph(Digraph)
    sp = BFSshortestpath(g, g.getNode(source), g.getNode(destination),
                         to_print=True)
    if sp is not None:
        print('\nShortest path from', source, 'to', destination, 'is\n', printPath(sp))
    else:
        print('There is no path from', source, 'to', destination)


BFStestSP('Boston', 'Phoenix')

'''
OUTPUT : 

Adjacency list is as follows :
 Boston --> Providence
Boston --> New York
Providence --> Boston
Providence --> New York
New York --> Chicago
Chicago --> Phoenix
Chicago --> Denver
Denver --> Phoenix
Denver --> New York
Los Angeles --> Boston 


Current DFS Path :  Boston
Current DFS Path :  Boston --> Providence
Node already visited. Skipping...
Current DFS Path :  Boston --> Providence --> New York
Current DFS Path :  Boston --> Providence --> New York --> Chicago
Current DFS Path :  Boston --> Providence --> New York --> Chicago --> Phoenix
Current DFS Path :  Boston --> Providence --> New York --> Chicago --> Denver
Node already visited. Skipping...
Current DFS Path :  Boston --> New York
Current DFS Path :  Boston --> New York --> Chicago
Current DFS Path :  Boston --> New York --> Chicago --> Phoenix
Current DFS Path :  Boston --> New York --> Chicago --> Denver
Node already visited. Skipping...

Shortest path from Boston to Phoenix is
 Boston --> New York --> Chicago --> Phoenix

Current BFS Path :  Boston
Current BFS Path :  Boston --> Providence
Current BFS Path :  Boston --> New York
Current BFS Path :  Boston --> Providence --> New York
Current BFS Path :  Boston --> New York --> Chicago
Current BFS Path :  Boston --> Providence --> New York --> Chicago
Current BFS Path :  Boston --> New York --> Chicago --> Phoenix

Shortest path from Boston to Phoenix is
 Boston --> New York --> Chicago --> Phoenix

'''