from graph2 import *
from var import *
from stop import *
from path import *
import time


def view():
    print("-----------------------------API-----------------------------")
    print("a) Find shortest path from a stop x to stop y")
    print("b) Find all pairs shortest path")
    print("c) Top ten most important stops")
    print("d) Exit")
    print("-------------------------------------------------------------")
    
def view2():
    print("1. Dijkstra's algorithm")
    print("2. D'Esopo-Pape's algorithm")

def run_conversation():
    graph = Graph2("vars.json", "stops.json", "paths.json")
    while True:
        view()
        choice1 = input("Enter your choice (a, b, c): ")
        if choice1 == "d":
            print("Goodbye!")
            break
        elif choice1 != "a" and choice1 != "b" and choice1 != "c":
            print("Invalid choice")
            continue
        view2()
        choice2 = int(input("Enter your choice (1, 2): "))
        
        if choice1 == "a":
            if choice2 == 1:
                x = int(input("Enter stop x: "))
                y = int(input("Enter stop x: "))
                dist, trace = graph.dijkstraOne(x)
                graph.findShortestPath(dist, trace, x, y)
            else:
                x = int(input("Enter stop x: "))
                y = int(input("Enter stop x: "))
                dist, trace, cnt = graph.desopoPage(x)
                graph.findShortestPath(dist, trace, x, y)
        elif choice1 == "b":
            if choice2 == 1:
                graph.dijkstraAll()
                graph.saveAllFile()
            else:
                graph.desopoPageAll()
                graph.saveAllFile()
        elif choice1 == "c":
            if choice2 == 1:
                graph.dijkstraAll()
                graph.topTenImpoStopsDijkstra()
            else:
                graph.desopoPageAll()
                graph.topTenImpoStopsDesopoPage()     
    

def benchMarkDijkstra():
    longestTime = -1e9
    fastestTime = 1e9
    averageTime = 0

    graph = Graph2("vars.json", "stops.json", "paths.json")
    for x in graph.numVertices:
        startTime = time.time()
        dist, trace = graph.dijkstraOne(x)
        endTime = time.time()
        executionTime = endTime - startTime
        averageTime += executionTime
        if executionTime > longestTime:
            longestTime = executionTime
        if executionTime < fastestTime and executionTime > 0:
            fastestTime = executionTime
    
    averageTime = averageTime / len(graph.numVertices)
    
    return fastestTime, longestTime, averageTime
        
def benchMarkDesopoPage():
    longestTime = -1e9
    fastestTime = 1e9
    averageTime = 0

    graph = Graph2("vars.json", "stops.json", "paths.json")
    for x in graph.numVertices:
        startTime = time.time()
        dist, trace, cnt = graph.desopoPage(x)
        endTime = time.time()
        executionTime = endTime - startTime
        averageTime += executionTime
        if executionTime > longestTime:
            longestTime = executionTime
        if executionTime < fastestTime and executionTime > 0:
            fastestTime = executionTime
    
    averageTime = averageTime / len(graph.numVertices)
    
    return fastestTime, longestTime, averageTime
    
    