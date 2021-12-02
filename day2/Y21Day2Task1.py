# Advent of Code Day 1 part 1
# Part 1
import numpy as np

file1 = open('inputday2.txt', 'r')
data = []


file1 = open('inputday2.txt', 'r')
data = file1.readlines()

for i in range(len(data)):
    data[i] = data[i].strip()
print(data)
file1.close()

horizontal = 0
vertical = 0

for j in range(len(data)):
    line = data[j].split(' ')
    print(line)
    if line[0] == "forward":
        horizontal  = horizontal + int(line[1])
    if line[0] == "up":
        vertical = vertical + int(line[1])
    if line[0] == "down":
        vertical = vertical - int(line[1])

answer1 = vertical*horizontal
print(answer1)

