import re
inputInLines = open('input.txt', 'r').readlines()
instructionString = ''
nodeMapDict = {}

for index, line in enumerate(inputInLines):
    if index == 0:
        instructionString = line.rstrip()
        continue
    elif index == 1:
        continue
    lineNodes = re.findall(r'[^\s=(),]+', line)
    nodeMapDict[lineNodes[0]] = [lineNodes[1], lineNodes[2]]

currentNode = 'AAA'
reachedEnd = False
steps = 0

while reachedEnd == False:
    for character in instructionString:
        if character == 'L':
            currentNode = nodeMapDict[currentNode][0]
            steps += 1
        else:
            currentNode = nodeMapDict[currentNode][1]
            steps += 1
        if currentNode == 'ZZZ':
            reachedEnd = True

print(steps)