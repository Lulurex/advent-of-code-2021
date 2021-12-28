# Advent of Code Day 12 part 1
# Part 1

import numpy as np
#data = np.genfromtxt('day12test.txt')
#print(data)

f = open("day12test2.txt", "r")
listdata = f.read().splitlines()   # list of strings
#raw = [y for y in soraw]   # list of ints

print(listdata)
graph = {
    "test": "case"
}


CaveDict = {}
Verticies = []

class Cave:                     # Every cave will be an object
    def __init__(self):
        self.size = "small"     # That has a size
        self.connectedTo = []   # And what it's connected to

    def getConnectionList(self):    # How to retrieve the list
        print(self.connectedTo)

    def addConnection(self,newCave):    # How to add a cave
        self.connectedTo.append(newCave)

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
        print("adding: " + a[0])

    else:
        print("skip " + a[0])

print("which cave do you want to inspect?")
whichcave = input()

c = CaveDict[whichcave]
print(c.size)
print(c.connectedTo)
print("~~~")
#print("all keys")
#print(CaveDict.keys())



#print(graph)


#potato = Cave()
#potato.addConnection("AB")
#potato.addConnection("AC")
#print(potato.connectedTo)
#print(potato.size)

#tomato = Cave()
#tomato.size = "big"
#print(tomato.size)


#print(Verticies)
#print(graph)

# obtain the connections