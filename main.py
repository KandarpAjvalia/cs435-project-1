import random
from graph import Graph


class Main:
    @staticmethod
    def createRandomUnweightedGraph(n):
        graph = Graph()
        nums = list(range(n))
        for num in nums:
            graph.addNode(num)
        random.shuffle(nums)
        for nodeVal in graph.nodes:
            numEdges = random.randint(0, n - 1)
            random.shuffle(nums)
            for num in nums[:numEdges]:
                if num != nodeVal:
                    node1 = graph.getNode(nodeVal)
                    node2 = graph.getNode(num)
                    graph.addUndirectedEdge(node1, node2)
        return graph

    @staticmethod
    def createLinkedList(n):
        linkedListGraph = Graph()
        nums = list(range(n))
        for num in nums:
            linkedListGraph.addNode(num)
        for i in range(0, len(nums) - 1):
            node1 = linkedListGraph.getNode(nums[i])
            node2 = linkedListGraph.getNode(nums[i + 1])
            linkedListGraph.addUndirectedEdge(node1, node2)
        return linkedListGraph

    @staticmethod
    def BFTRecLinkedList(graph):
        from graphSearch import GraphSearch
        return GraphSearch.BFTRec(graph)

    @staticmethod
    def BFTIterLinkedList(graph):
        from graphSearch import GraphSearch
        return GraphSearch.BFSIter(graph)


if __name__ == "__main__":
    m = Main
    print()
    print('3 b -------------------- Random Unweighted Graph')
    print(m.createRandomUnweightedGraph(10))
    print()
    print('3 c -------------------- Linked List Graph')
    print(m.createLinkedList(10))
    print()
