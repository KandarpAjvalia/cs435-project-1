import random
from graph import Graph


class Main:
    @staticmethod
    def createRandomUnweightedGraph(n):
        graph = Graph()
        nums = list(range(n))
        random.shuffle(nums)
        for num in nums:
            graph.addNode(num)
        for node in graph.nodes:
            numEdges = random.randint(0, n - 1)
            random.shuffle(nums)
            for num in nums[:numEdges]:
                if num != node:
                    graph.addUndirectedEdge(node, num)

        return graph


print(Main.createRandomUnweightedGraph(10))
