from gridNode import GridNode

class GridGraph:
    """
    {
       'a': {'b': 1, 'c': 1},
       'c': {'a': 1},
       'b': {'a': 1}
    }
    """
    def __init__(self):
        self.nodes = set()
        self.vals = {}

    def addNode(self, x, y, nodeVal):
        if nodeVal not in self.vals:
            node = GridNode(x, y, nodeVal)
            self.vals[nodeVal] = node
            self.nodes.add(node)

    def addUndirectedEdge(self, first, second):
        if isinstance(first, GridNode) and isinstance(second, GridNode) and first in self.nodes and second in self.nodes:
            first.addNeighbor(second)
            second.addNeighbor(first)

    def removeUndirectedEdge(self, first, second):
        if isinstance(first, GridNode) and isinstance(second, GridNode) and first in self.nodes and second in self.nodes:
            first.removeNeighbor(second)
            second.removeNeighbor(first)

    def getNode(self, nodeVal):
        if nodeVal in self.vals:
            return self.vals[nodeVal]

    # node is an actual node not a value/number
    def getNeighbors(self, node):
        return node.getNeighbors()

    def getAllNodes(self):
        return set(self.nodes)

    def __str__(self):
        s = ''
        for node in self.nodes:
            s += str(node)
        return s

if __name__ == '__main__':
    graph = GridGraph()
    print('x, y, val')
    graph.addNode(1, 0, 1)
    graph.addNode(0, 1, 0)
    print(graph)
    # print(graph.getNeighbors(graph.getNode(1)))
    firstNode = graph.getNode(0)
    secondNode = graph.getNode(1)
    graph.addUndirectedEdge(firstNode, secondNode)
    print(graph)
    graph.removeUndirectedEdge(firstNode, secondNode)
    print(graph)