
class Graph:
    """
    {
       'a': {'b': 1, 'c': 3},
       'c': {'a': 3},
       'b': {'a': 1}
    }
    """
    def __init__(self):
        self.nodes = {}

    def addNode(self, nodeVal):
        if nodeVal not in self.nodes:
            self.nodes[nodeVal] = {}

    def addConnection(self, first, second, weight=1):
        self.nodes[first][second] = weight
        self.nodes[second][first] = weight

    def addUndirectedEdge(self, first, second):
        if first in self.nodes and second in self.nodes:
            self.addConnection(first, second)

    def removeUndirectedEdge(self, first, second):
        if first in self.nodes and second in self.nodes:
            self.nodes[first].pop(second, None)
            self.nodes[second].pop(first, None)

    def getAllNodes(self):
        return set(self.nodes)

    def __str__(self):
        s = ''
        for node, connections in self.nodes.items():
            s += '{}:  {}\n'.format(str(node), connections)
        return s

if __name__ == "__main__":
    graph = Graph()

    print()
    print('3 a i -------------------- Add Nodes')
    graph.addNode('a')
    graph.addNode('b')
    print(graph)

    print('3 a ii -------------------- Add Undirected Edge')
    graph.addUndirectedEdge('a', 'b')
    print(graph)

    print('3 a iii -------------------- Remove Undirected Edge')
    graph.removeUndirectedEdge('a', 'b')
    print(graph)

    print('3 a iv -------------------- Get All Nodes')
    print(graph.getAllNodes())
    print()