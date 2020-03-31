from node import Node

class Graph:
    """
    {
       'a': {<NodeObject>},
       'c': {<NodeObject>},
       'b': {}
    }
    """
    def __init__(self):
        self.nodes = {}

    def addNode(self, nodeVal):
        if nodeVal not in self.nodes:
            self.nodes[nodeVal] = Node(nodeVal)

    def addUndirectedEdge(self, first, second):
        if isinstance(first, Node) and isinstance(second,
                                                  Node) and first.val in self.nodes and second.val in self.nodes:
            first.addNeighbor(second)
            second.addNeighbor(first)

    def removeUndirectedEdge(self, first, second):
        if isinstance(first, Node) and isinstance(second,
                                                  Node) and first.val in self.nodes and second.val in self.nodes:
            first.removeNeighbor(second)
            second.removeNeighbor(first)

    @staticmethod
    def getNode(node, val):
        return self.nodes[val]

    def getAllNodes(self):
        return set(self.nodes)

    def __str__(self):
        s = ''
        for nodeVal, node in self.nodes.items():
            s += '{}:  {}\n'.format(nodeVal, node)
        return s


if __name__ == "__main__":
    graph = Graph()

    print()
    print('3 a i -------------------- Add Nodes')
    graph.addNode('a')
    graph.addNode('b')
    print(graph)

    print('3 a ii -------------------- Add Undirected Edge')
    a = graph.getNode('a')
    b = graph.getNode('b')
    graph.addUndirectedEdge(a, b)
    print(a.getNeighbors())
    print(graph)

    print('3 a iii -------------------- Remove Undirected Edge')
    graph.removeUndirectedEdge(a, b)
    print(graph)

    # print('3 a iv -------------------- Get All Nodes')
    # print(graph.getAllNodes())
    # print()