import random
import sys
from weightedGraph import WeightedGraph
import heapq
import json


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

        for i in range(n - 1):
            graph.addWeightedEdge(i, i + 1, 1)

        return graph

    @staticmethod
    def dijkstras(graph, start):
        nodeDistanceMap = {}
        weightNodeTupleList = [(0, start)]
        valsInHeap = set()
        valsInHeap.add(start)
        allNodes = set()
        allNodes.add(start)
        while weightNodeTupleList:
            heapq.heapify(weightNodeTupleList)
            weightNodeTuple = heapq.heappop(weightNodeTupleList)
            currWeight = weightNodeTuple[0]
            curr = weightNodeTuple[1]
            nodeDistanceMap[curr] = currWeight
            valsInHeap.remove(curr)

            for node, weight in graph.getNeighbors(curr).items():
                if node not in allNodes:
                    allNodes.add(node)
                    weightNodeTupleList.append((sys.maxsize, node))
                    valsInHeap.add(node)

                if node not in valsInHeap:
                    continue

                newDistance = currWeight + weight

                index = Main.findNode(weightNodeTupleList, node)
                if newDistance < weightNodeTupleList[index][0]:
                    weightNodeTupleList[index] = (newDistance, node)

        return nodeDistanceMap

    @staticmethod
    def findNode(tupleList, node):
        for i in range(len(tupleList)):
            if tupleList[i][1] == node:
                return i


if __name__ == '__main__':
    print()
    print('5 d -------------------- Random Complete Weighted Graph')
    graph = Main.createRandomCompleteWeightedGraph(6)
    print(graph)

    print()
    print('5 e i -------------------- Djikstra on Random Complete Weighted Graph, start = 1')
    distancesFromNode = Main.dijkstras(graph, 1)
    print(json.dumps(distancesFromNode, indent=4, sort_keys=True))

    print()
    print('5 d -------------------- Create LinkedList')
    linkedList = Main.createLinkedList(5)
    print(linkedList)

    print()
    print('5 e ii -------------------- Djikstra on Linked List, start = 0')
    distancesFromNode = Main.dijkstras(linkedList, 0)
    print(json.dumps(distancesFromNode, indent=4, sort_keys=True))
    print()
