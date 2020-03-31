import random

from directedGraph import DirectedGraph

class Main:
    @staticmethod
    def createRandomDAGIter(n):
        graph = DirectedGraph()
        nums = list(range(n))
        for num in nums:
            graph.addNode(num)

        for node in graph.nodes:
            for i in range(node + 1, n):
                if random.randint(0, 1):
                    graph.addDirectedEdge(node, i)

        return graph


if __name__ == "__main__":
    m = Main
    print()
    print('4 c -------------------- Random Directed Graph')
    print(m.createRandomDAGIter(10))