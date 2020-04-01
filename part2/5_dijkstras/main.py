import random
from weightedGraph import WeightedGraph

class Main:

    @staticmethod
    def createRandomCompleteWeightedGraph(n):
        graph = WeightedGraph()
        for i in range(n):
            graph.addNode(i)

        for node in graph.getAllNodes():
            for i in range(n):
                if node != i:
                    graph.addWeightedEdge(node, i, random.randint(1, 20))

        return graph

    @staticmethod
    def createLinkedList(n):
        graph = WeightedGraph()
        for i in range(n):
            graph.addNode(i)

        for i in  range(n - 1):
            graph.addWeightedEdge(i, i + 1, 1)

        return graph

if __name__=='__main__':
    print()
    print('5 c -------------------- Random Complete Weighted Graph')
    graph = Main.createRandomCompleteWeightedGraph(5)
    print(graph)
    print()
    print('5 d -------------------- Create LinkedList')
    graph = Main.createLinkedList(5)
    print(graph)