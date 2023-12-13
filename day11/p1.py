input = open('input.txt', 'r').readlines()
galaxiesMatrix = []

for line in input:
    galaxiesMatrix.append(list(line.strip()))
    emptyRow = True
    for char in list(line.strip()):
        if char != '.':
            emptyRow = False
    if emptyRow:
        galaxiesMatrix.append(list(line.strip()))

columnsToAdd = []
for columnIndex, column in enumerate(galaxiesMatrix[0]):
    emptyColumn = True
    for row in galaxiesMatrix:
        if row[columnIndex] != '.':
            emptyColumn = False
    if emptyColumn:
        columnsToAdd.append(columnIndex)

for row in galaxiesMatrix:
    for index in reversed(columnsToAdd):
        row.insert(index, '.')

galaxyCounter = 0
galaxyAddresses = {}
galaxiesList = []
for rIndex, row in enumerate(galaxiesMatrix):
    for cIndex, char in enumerate(row):
        if char == '#':
            galaxyCounter += 1
            row[cIndex] = galaxyCounter
            galaxyAddresses[str(galaxyCounter)] = [rIndex, cIndex]
            galaxiesList.append(galaxyCounter)

totalPathLengths = 0
while len(galaxiesList) > 1:
    workingGalaxy = galaxiesList.pop(0)
    for otherGalaxy in galaxiesList:
        rowDiff = galaxyAddresses[str(otherGalaxy)][0] - galaxyAddresses[str(workingGalaxy)][0]
        columnDiff = galaxyAddresses[str(otherGalaxy)][1] - galaxyAddresses[str(workingGalaxy)][1]
        pathLength = abs(rowDiff) + abs(columnDiff)
        totalPathLengths += pathLength

print(totalPathLengths)