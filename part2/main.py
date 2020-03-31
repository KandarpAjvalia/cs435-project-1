import random

from directedGraph import DirectedGraph

class Main:
    @staticmethod
    def createRandomDAGIter(n):
        graph = DirectedGraph()
        nums = list(range(n))
        for num in nums:
            graph.addNode(num)

        for node in graph.getAllNodes():
            numNodes = random.randint(0, n - node)
            numsAdded = set()
            while len(numsAdded) != numNodes:
                num = random.randint(node + 1, n)
                if num not in numsAdded:
                    numsAdded.add(num)
                    graph.addDirectedEdge(node, num)

        return graph


if __name__ == "__main__":
    m = Main
    print()
    print('4 c -------------------- Random Directed Graph')
    print(m.createRandomDAGIter(10))