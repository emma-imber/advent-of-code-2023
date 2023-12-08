import re
import math

inputInLines = open('input.txt', 'r').readlines()
instructionString = ''
nodeMapDict = {}
startNodes = []

for index, line in enumerate(inputInLines):
    if index == 0:
        instructionString = line.rstrip()
        continue
    elif index == 1:
        continue
    lineNodes = re.findall(r'[^\s=(),]+', line)
    nodeMapDict[lineNodes[0]] = [lineNodes[1], lineNodes[2]]
    if lineNodes[0][-1] == 'A':
        startNodes.append(lineNodes[0])

reachedEnd = False
periods = []

for index, node in enumerate(startNodes):
    steps = 0
    currentNode = node
    reachedEnd = False
    while reachedEnd == False:
        for character in instructionString:
            if character == 'L':
                currentNode = nodeMapDict[currentNode][0]
                steps += 1
            else:
                currentNode = nodeMapDict[currentNode][1]
                steps += 1
            if currentNode[-1] == 'Z':
                reachedEnd = True
                periods.append(steps)

print(math.lcm(*periods))