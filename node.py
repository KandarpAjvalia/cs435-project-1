class graphNode:
    def __init__(self, val):
        self.val = val
        self.connected = {}

    def addConnection(self, node, weight=1):
        self.connected[node] = weight

    def __str__(self):
        return str(self.connected)
