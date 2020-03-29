from main import Main


class GraphSearch:

    @staticmethod
    def DFSRec(graph, start, end, path=None, visited=None):
        if visited is None:
            visited = set()
        if path is None:
            path = []
        path.append(start)
        visited.add(start)
        if start == end:
            return True
        for node in graph.nodes[start]:
            if node not in visited:
                found = GraphSearch.DFSRec(graph, node, end, path, visited)
                if found:
                    return path
        return None

    @staticmethod
    def DFSIter(graph, start, end):
        pass

    @staticmethod
    def BFSRec():
        pass

    @staticmethod
    def BFSIter():
        pass


graph = Main.createLinkedList(10)
# graph = Main.createRandomUnweightedGraph(10)
print(graph)
# print(graph.nodes[1])
print(GraphSearch.DFSRec(graph, 3, 9))
