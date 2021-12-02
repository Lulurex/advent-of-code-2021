# Advent of Code Day 1 part 1
# Part 1
import numpy as np
data = np.genfromtxt('inputday1.txt')
print(data)

pcounter = 0

for i in range(len(data)-1):
    if data[i] < data[i+1]:
        pcounter += 1
    else:
        pass
print(pcounter)

# Part 2

a = data[0]
b = data[1]
c = data[2]
d = data[3]
previous_sum = a + b + c
next_sum = b + c + d
inc_counter = 0
for i in range(3,len(data)):
        d = data[i]
        previous_sum = a + b + c
        next_sum = b + c + d
        if previous_sum < next_sum:
            inc_counter += 1
        a = b
        b = c
        c = d
        i += 1

print(inc_counter)
