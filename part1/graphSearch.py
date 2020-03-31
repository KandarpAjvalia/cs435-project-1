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
        for node in graph.getNeighbors(start):
            if node not in visited:
                found = GraphSearch.DFSRec(graph, node, end, path, visited)
                if found:
                    return path
        return None

    @staticmethod
    def DFSIter(graph, start, end):
        if start == end:
            return [start]
        stackSim = [start]
        visited = set()
        path = []
        while stackSim:
            curr = stackSim.pop()
            path.append(curr)
            if curr == end:
                return path
            visited.add(curr)
            for node in graph.getNeighbors(curr):
                if node not in visited:
                    stackSim.append(node)
        return None

    @staticmethod
    def BFTRec(graph):

        path = []
        queue = []
        visited = set()
        GraphSearch.BFTRecHelper(graph, path, queue, visited)
        for node in graph.getAllNodes():
            if node not in visited:
                visited.add(node)
                queue.append(node)
                GraphSearch.BFTRecHelper(graph, path, queue, visited)
        return path

    @staticmethod
    def BFTRecHelper(graph, path, queue, visited):
        if not queue:
            return
        curr = queue.pop(0)
        path.append(curr)
        for node in graph.getNeighbors(curr):
            if node not in visited:
                visited.add(node)
                queue.append(node)
        GraphSearch.BFTRecHelper(graph, path, queue, visited)

    @staticmethod
    def BFSIter(graph):
        queue = []
        path = []
        visited = set()
        for node in graph.getAllNodes():
            if node not in visited:
                visited.add(node)
                queue.append(node)
                while queue:
                    curr = queue.pop(0)
                    path.append(curr)
                    for nestedNode in graph.getNeighbors(curr):
                        if nestedNode not in visited:
                            visited.add(nestedNode)
                            queue.append(nestedNode)
        return path


if __name__=='__main__':
    graph = Main.createRandomUnweightedGraph(10)

    print('\nGraph representation:--------------------')
    print(graph)

    print('3 d -------------------- DFS Recursive on above graph ----- Search 3--->7')
    print(GraphSearch.DFSRec(graph, 3, 7))
    print()
    print('3 e -------------------- DFS Iterative on above graph ----- Search 3--->7')
    print(GraphSearch.DFSIter(graph, 3, 7))
    print()
    print('3 f -------------------- BFT Recursive on above graph')
    print(GraphSearch.BFTRec(graph))
    print()
    print('3 g -------------------- BFT Iterative on above graph')
    print(GraphSearch.BFSIter(graph))
    graph = Main.createLinkedList(10000)
    print()
    # print('3 h -------------------- BFT Recursive on LinkedList 10000 nodes')
    # print(Main.BFTRecLinkedList(graph))
    # print()
    print('3 i -------------------- BFT Iterative on LinkedList 10000 nodes')
    print(Main.BFTIterLinkedList(graph))
    print('\n')
