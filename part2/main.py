import random

from directedGraph import DirectedGraph

class Main:
    @staticmethod
    def createRandomDAGIter(n):
        graph = DirectedGraph()
        nums = list(range(n))
        for num in nums:
            graph.addNode(num)
        random.shuffle(nums)
        for node in graph.nodes:
            numEdges = random.randint(0, n - 1) // random.randint(1, n//10)
            random.shuffle(nums)
            for num in nums[:numEdges]:
                if num != node:
                    graph.addDirectedEdge(node, num)
        return graph


if __name__ == "__main__":
    m = Main
    print()
    print('4 c -------------------- Random Directed Graph')
    print(m.createRandomDAGIter(10))