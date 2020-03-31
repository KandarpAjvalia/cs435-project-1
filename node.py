class Node:
    """
    {
        val: 1,
        neighbors: {<NodeObject>, <NodeObject>}
            alt
            neighbors: {val: neighbors, val2: neighbors}
    }
    """

    def __init__(self, val):
        self.val = val
        self.neighbors = set()

    def getNeighbors(self):
        return self.neighbors

    def addNeighbor(self, neighborNode):
        self.neighbors.add(neighborNode)

    def removeNeighbor(self, nodeToRemove):
        self.neighbors.remove(nodeToRemove)

    def __str__(self):
        # print(set(self.neighbors.keys()))
        # # for value, node in self.neighbors.items():
        # #     s += '' str(value)
        s = self.neighbors
        print()
        return str(self.val) + ': ' + (str(s) if s else '{}')
