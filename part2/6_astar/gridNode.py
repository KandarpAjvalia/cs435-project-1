class GridNode:
    def __init__(self, x, y, val):
        self.x = x
        self.y = y
        self.val = val
        self.neighbors = set()

    def addNeighbor(self, node):
        self.neighbors.add(node)

    def getNeighbors(self):
        return self.neighbors

    def removeNeighbor(self, node):
        self.neighbors.remove(node)

    def __str__(self):
        # s = str((self.x, self.y, self.val)) + ':  '
        s = str(self.val) + ': ['
        # print(self.neighbors)
        for neighbor in self.neighbors:
            s += str(neighbor.val) + ', '
        # s += str(self.neighbors) + '\n' if self.neighbors else 'No Neighbors\n'
        s += ']\n'
        return s
