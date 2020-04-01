from main import Main


class TopSort:

    @staticmethod
    def getIndegrees(graph):
        indegrees = [0] * len(graph.nodes)
        for node in graph.getAllNodes():
            for nestedNode in graph.getNeighbors(node):
                indegrees[nestedNode] += 1
        return indegrees

    @staticmethod
    def Kahns(graph):
        indegrees = TopSort.getIndegrees(graph)
        queue = []
        for i in range(len(indegrees)):
            if indegrees[i] == 0:
                queue.append(i)

        kahnsSorted = []
        while queue:
            curr = queue.pop(0)
            kahnsSorted.append(curr)
            for node in graph.getNeighbors(curr):
                indegrees[node] -= 1
                if indegrees[node] == 0:
                    queue.append(node)

        return kahnsSorted

    @staticmethod
    def mDFS(graph):
        stackSim = []
        visited = set()
        for node in graph.getAllNodes():
            if node not in visited:
                TopSort.DFSHelper(graph, node, stackSim, visited)
        return stackSim[::-1]

    @staticmethod
    def DFSHelper(graph, node, stackSim, visited):
        visited.add(node)
        for nestedNode in graph.getNeighbors(node):
            if nestedNode not in visited:
                TopSort.DFSHelper(graph, nestedNode, stackSim, visited)
        stackSim.append(node)

if __name__ == '__main__':
    graph = Main.createRandomDAGIter(1000)
    print(graph)
    print('4 d -------------------- Kahn\'s Algorithm on above Graph')
    print(TopSort.Kahns(graph))
    print()
    print('4 e -------------------- mDFS on above Graph')
    print(TopSort.mDFS(graph))
    print()
