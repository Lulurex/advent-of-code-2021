# Advent of Code Day 12 part 1
# Part 1

import numpy as np
#data = np.genfromtxt('day12test.txt')
#print(data)

f = open("day12test.txt", "r")
listdata = f.read().splitlines()   # list of strings
#raw = [y for y in soraw]   # list of ints

graph = {}
CaveDict = {}
Verticies = []
count = 0

def inspectCave():
    print("which cave do you want to inspect?")
    whichcave = input()

    c = CaveDict[whichcave]
    print(c.size)
    print(c.connectedTo)
    print("~~~")


class Cave:                     # Every cave will be an object
    def __init__(self):
        self.size = "small"     # That has a size
        self.connectedTo = []   # And what it's connected to

    def getConnectionList(self):    # How to retrieve the list
        print(self.connectedTo)

    def addConnection(self,newCave):    # How to add a cave
        self.connectedTo.append(newCave)

    def removeConnection(self,removethiscave):
        self.connectedTo.remove(removethiscave)

# Make each cave into a class, note if it's a big cave and what it's connected to
for entry in listdata:

    a = entry.split("-")
    cavename = a[0]
    if a[0] not in CaveDict:
        CaveDict[cavename] = Cave() # New Cave

    c = CaveDict[cavename]
    c.addConnection(a[1])

    if cavename.isupper() == True:
        c.size = "big"



    cavename = a[1]
    if a[1] not in CaveDict:
        CaveDict[cavename] = Cave()

    c = CaveDict[cavename]
    c.addConnection(a[0])

    if cavename.isupper() == True:
        c.size = "big"


    if a[0] not in Verticies:
        Verticies.append(a[0])      # Append the vertex to the LIST
    if a[1] not in Verticies:
        Verticies.append(a[1])

#print("all keys")
#print(CaveDict.keys())

# inspectCave()

for vertex in Verticies:
    c = CaveDict[vertex]
    graph[vertex] = c.connectedTo

small_caves = []
for key in graph.keys():
    if key.islower() == True:
        small_caves.append(key)
print("small caves: " + str(small_caves))

#print(graph)
paths = []
starting_cavename = "start"

def find_path(graph, start, end, path = []):
    path = path + [start]
    #print("start: " + start)
    #print("path: " + str(path))
    if start == end:
        #print("Destination FOUND")
        global count
        count += 1
        global paths
        paths.append(path)
        return path
    if len(graph[start]) == 1 and start.isupper() == True:
        #print("DEAD END! going back...")
        return []
    helper = graph[start]
    print(helper)
    for node in graph[start]:
        # if        new      and        small          or (     big )
        if (node not in path and node in small_caves) or (node not in small_caves):
            #print("node, path")
            #print(node)
            #print(path)
            find_path(graph, node, end, path)



find_path(graph, starting_cavename, "end")
print("There are " + str(count) + " caves in this system.")
print("Here are the paths: ")
print(paths)


''' PART TWO'''

def checkForDoubles(double, path):
    doubleDict = {}
    for item in path:
        if len(doubleDict[itme]) == "2":
            print("new key")
            doubleDict[item] = "2"
        else:
            print("B")

paths = []
starting_cavename = "start"
count = 0
small_caves = []
for key in graph.keys():
    if key == "start":
        continue
    if key == "end":
        continue
    if key.islower() == True:
        small_caves.append(key)
print("small caves: " + str(small_caves))

one_time_cave = ["start", "end"]
double_cave = ""

def find_path_p2(graph, start, end, path = []):
    path = path + [start]
    #print("start: " + start)
    #print("path: " + str(path))
    if start == end:
        print("Destination FOUND")
        global count
        count += 1
        global paths
        paths.append(path)
        return path
    if len(graph[start]) == 1 and start.isupper() == True:
        print("DEAD END! going back...")
        return []
    for node in graph[start]:
        #               small   and not      start/finish     or    big
        if (node in small_caves and not one_time_cave) or (node not in small_caves and not small_caves):
            checkForDoubles(path)
            #print("node, path")
            #print(node)
            #print(path)

            find_path_p2(graph, node, end, path)
    return None


#find_path_p2(graph, starting_cavename, "end")
print(count)
print(paths)