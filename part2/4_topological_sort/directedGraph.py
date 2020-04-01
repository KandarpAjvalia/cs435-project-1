
class DirectedGraph:
    """
    {
       'a': {'b': 1},
       'c': {'a': 3},
       'b': {}
    }
    """
    def __init__(self):
        self.nodes = {}

    def addNode(self, nodeVal):
        if nodeVal not in self.nodes:
            self.nodes[nodeVal] = {}

    def addConnection(self, first, second, weight=1):
        self.nodes[first][second] = weight

    def addDirectedEdge(self, first, second):
        if first in self.nodes and second in self.nodes:
            self.addConnection(first, second)

    def removeDirectedEdge(self, first, second):
        if first in self.nodes:
            self.nodes[first].pop(second, None)

    def getAllNodes(self):
        return set(self.nodes)

    def getNeighbors(self, node):
        return self.nodes[node]

    def __str__(self):
        s = ''
        for node, connections in self.nodes.items():
            s += '{}:  {}\n'.format(str(node), connections)
        return s


if __name__ == "__main__":
    graph = DirectedGraph()

    print()
    print('4 b i -------------------- Add Nodes')
    graph.addNode('a')
    graph.addNode('b')
    print(graph)

    print('4 b ii -------------------- Add Directed Edge')
    graph.addDirectedEdge('a', 'b')
    print(graph)

    print('4 b iii -------------------- Remove Directed Edge')
    graph.removeDirectedEdge('a', 'b')
    print(graph)

    print('4 b iv -------------------- Get All Nodes')
    print(graph.getAllNodes())
    print()