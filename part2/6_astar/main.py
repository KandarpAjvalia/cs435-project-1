import random
import math
import heapq
import sys
import time
from gridGraph import GridGraph

class Main:

    @staticmethod
    def getNeighbors(arr, j, i):
        n = len(arr)
        neighbors = []
        for a in range(max(0, i - 1), min(i + 1, n - 1) + 1):
            for b in range(max(0, j - 1), min(j + 1, n - 1) + 1):
                if (a != i or b != j) and not (a != i and b != j):
                    neighbors.append(arr[a][b])
        return neighbors

    @staticmethod
    def createRandomGridGraph(n):
        graph = GridGraph()
        arr = [[0 for j in range(n)] for i in range(n)]
        i = 0
        for r in range(n):
            for c in range(n):
                graph.addNode(c, r, i)
                arr[r][c] = i
                i += 1

        for num in range(n**2):
            node = graph.getNode(num)

            neighbors = Main.getNeighbors(arr, node.x, node.y)

            for neighbor in neighbors:
                if random.randint(0, 1):

                    node2 = graph.getNode(neighbor)
                    graph.addUndirectedEdge(node, node2)
        return graph

    @staticmethod
    def heuristic(node, end):
        # using Manhattan Distance Heuristic
        x1, y1 = end.x, end.y
        x2, y2 = node.x, node.y
        return abs(x1 - x2) + abs(y1 - y2)

    @staticmethod
    def astar(graph, start, end):
        # f score is the sum of g score and h score
        # g score is the cost of current path from start to current node
        # h score is the cost from current node to the end node
        fScoreNodeTupleList = [(0, start.val)]
        gScores = {start.val: 0}
        fScores = {start.val: Main.heuristic(start, end)}
        allNodes = set()
        allNodes.add(start)
        visited = set()
        path = {}
        while fScoreNodeTupleList:
            # heapq.heapify(fScoreNodeTupleList)
            weightNodeTuple = heapq.heappop(fScoreNodeTupleList)
            curr = weightNodeTuple[1]
            visited.add(curr)
            if curr == end.val:
                createPath = [end.val]
                temp = path[end.val]
                while temp != start.val:
                    createPath.insert(0, temp)
                    temp = path[temp]
                createPath.insert(0, start.val)
                return createPath

            for node in graph.getNode(curr).getNeighbors():
                if node not in allNodes:
                    allNodes.add(node)
                    heapq.heappush(fScoreNodeTupleList, (sys.maxsize, node.val))
                    gScores[node.val] = sys.maxsize
                    fScores[node.val] = sys.maxsize

                if gScores[curr] < gScores[node.val]:
                    path[node.val] = curr
                    gScores[node.val] = gScores[curr]
                    index = Main.findNode(fScoreNodeTupleList, node.val)
                    fScores[node.val] = gScores[node.val] + Main.heuristic(node, end)
                    if node not in visited:
                        fScoreNodeTupleList[index] = (gScores[node.val] + Main.heuristic(node, end), node.val)
        return []

    @staticmethod
    def findNode(tupleList, node):
        for i in range(len(tupleList)):
            if tupleList[i][1] == node:
                return i

if __name__ == '__main__':

    print()
    print('6 b -------------------- Random Grid Graph')
    randomGraph = Main.createRandomGridGraph(100)
    print(randomGraph)
    print()

    print('6 d -------------------- A* Search on above Grid Graph, Search 0 -> 8')
    startNode = randomGraph.getNode(0)
    endNode = randomGraph.getNode(9999)
    startAstar = time.time()
    aStarPath = Main.astar(randomGraph, startNode, endNode)
    print(aStarPath)
    print('\n')
    endAstar = time.time()
    print('7a -------------------- Edgextra Credit 1000 nodes')
    print('time: {} seconds'.format(endAstar - startAstar))
    print()