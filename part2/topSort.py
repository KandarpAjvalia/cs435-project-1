from main import Main


class TopSort:

    @staticmethod
    def getIndegrees(graph):
        indegrees = [0] * len(graph.nodes)
        for node in graph.nodes:
            for nestedNode in graph.nodes[node]:
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
            for node in graph.nodes[curr]:
                indegrees[node] -= 1
                if indegrees[node] == 0:
                    queue.append(node)

        return kahnsSorted

    @staticmethod
    def mDFS(graph):
        pass

if __name__ == '__main__':
    graph = Main.createRandomDAGIter(10)
    print(graph)
    print(TopSort.getIndegrees(graph))
    print(TopSort.Kahns(graph))
