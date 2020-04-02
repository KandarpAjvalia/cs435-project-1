import random
from gridGraph import GridGraph

class Main:

    @staticmethod
    def getNeighbors(arr, j, i):
        n = len(arr)
        neighbors = []
        for a in range(max(0, i - 1), min(i + 1, n - 1) + 1):
            for b in range(max(0, j - 1), min(j + 1, n - 1) + 1):
                if (a != i or b != j) and not (a != i and b != j):
                    neighbors.append(arr[a][b])
        return neighbors

    @staticmethod
    def createRandomGridGraph(n):
        graph = GridGraph()
        arr = [[0 for j in range(n)] for i in range(n)]
        i = 0
        for r in range(n):
            for c in range(n):
                graph.addNode(c, r, i)
                arr[r][c] = i
                i += 1

        alreadyAdded = set()
        for num in range(n**2):
            node = graph.getNode(num)

            print('val: {},  (x,y):({}, {})'.format(node.val, node.x, node.y))

            neighbors = Main.getNeighbors(arr, node.x, node.y)

            for neighbor in neighbors:
                if random.randint(0, 3) and neighbor not in alreadyAdded:
                    alreadyAdded.add(neighbor)
                    node2 = graph.getNode(neighbor)
                    graph.addUndirectedEdge(node, node2)

        return graph

if __name__ == '__main__':

    print()
    print('6 b -------------------- Random Grid Graph')
    randomGraph = Main.createRandomGridGraph(3)
    print(randomGraph)
    print()