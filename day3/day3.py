# Advent of Code Day 3 part 1
# Part 1

"""
Each bit in the gamma rate can be determined by finding the most common bit in the corresponding position of all numbers in the diagnostic report. For example, given the following diagnostic report:

00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010

Considering only the first bit of each number, there are five 0 bits and seven 1 bits. Since the most common bit is 1, the first bit of the gamma rate is 1.

The most common second bit of the numbers in the diagnostic report is 0, so the second bit of the gamma rate is 0.

The most common value of the third, fourth, and fifth bits are 1, 1, and 0, respectively, and so the final three bits of the gamma rate are 110.

So, the gamma rate is the binary number 10110, or 22 in decimal.

The epsilon rate is calculated in a similar way; rather than use the most common bit, the least common bit from each position is used. So, the epsilon rate is 01001, or 9 in decimal. Multiplying the gamma rate (22) by the epsilon rate (9) produces the power consumption, 198.

Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate, then multiply them together. What is the power consumption of the submarine? (Be sure to represent your answer in decimal, not binary.)



"""


"""
import numpy as np
data = np.genfromtxt('day3.txt')
print(data)
"""

f = open("day3.txt", "r")
listdata = f.read().splitlines()   # list of strings
#raw = [y for y in soraw]   # list of ints

LENGTH_OF_LINE = len(listdata[0])
LENGTH_OF_FILE = len(listdata)

# gamma  = most common bit
# epsilon = the flipped binary number

# Gamma
# create a bucket counter for the digits
count = []
while len(count) < LENGTH_OF_LINE:
    count.append(0)

i=0

# listdata[line][character]
for line in listdata:
    i = 0
    for char in line:
        if char == "1":
            count[i] += 1
            i+=1
        else:
            i+=1

print(count)
gamma = ""
epsilon = ""
k = 0
while k < LENGTH_OF_LINE:
    #print(count[k] >= LENGTH_OF_FILE/2)
    if count[k] >= LENGTH_OF_FILE/2: # 0 is dominant
        gamma = gamma + "1"
        epsilon = epsilon + "0"
    else:
        gamma = gamma + "0"
        epsilon = epsilon + "1"
    k += 1

#print(gamma)
#print(epsilon)

gammadec = int(gamma,2)
epsilondec = int(epsilon,2)

#print(gammadec)
#print(epsilondec)

soln1 = gammadec * epsilondec
print("soln1: " + str(soln1))

#OGR = ""
#C02 = ""

def getMostCommonBit(index, report, rate):
    #print(list)
    if len(report) == 1:
        print("final: ")
        print(report)
        if rate == "OGR":
            ogr = report[0]
            return ogr
        else:
            c02 = report[0]
            return c02


    #print("index: ")
    #print(index)
    pcount = []
    while len(pcount) < LENGTH_OF_LINE:
        pcount.append(0)

    # listdata[line][character]
    for line in report:
        l = 0
        for char in line:
            if char == "1":
                pcount[l] += 1
                l += 1
            else:
                l += 1


    if rate == "02":
        if pcount[index] >= len(report) / 2:  # 0 is dominant
            mcb = "1"
        else:
            mcb = "0"
        #print("mcb: " + str(mcb))
    else:
        if pcount[index] >= len(report) / 2:  # 0 is dominant
            mcb = "0"
        else:
            mcb = "1"
        #print("mcb: " + str(mcb))

    list_filtered = []
    for line_s in report:
        if line_s[index] == mcb:
            list_filtered.append(line_s)
            # print("adding: " + str(line_s))

    index += 1
    getMostCommonBit(index, list_filtered, rate)


getMostCommonBit(0, listdata, "02")
getMostCommonBit(0, listdata, "c0")

#print(type(OGR))

ogr = input()
c02 = input()

ogrdec = int(ogr,2)
c02dec = int(c02,2)

soln2 = ogrdec*c02dec
print("soln2: ")
print(soln2)



