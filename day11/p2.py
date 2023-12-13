input = open('input.txt', 'r').readlines()
galaxiesMatrix = []

rowsToAdd = []
for rowIndex, line in enumerate(input):
    galaxiesMatrix.append(list(line.strip()))
    emptyRow = True
    for char in list(line.strip()):
        if char != '.':
            emptyRow = False
    if emptyRow:
        rowsToAdd.append(rowIndex)

columnsToAdd = []
for columnIndex, column in enumerate(galaxiesMatrix[0]):
    emptyColumn = True
    for row in galaxiesMatrix:
        if row[columnIndex] != '.':
            emptyColumn = False
    if emptyColumn:
        columnsToAdd.append(columnIndex)
    
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

columnsAdded = 0
for column in columnsToAdd:
    newColumnValue = column + (columnsAdded * 999999)
    for galaxy in galaxyAddresses:
        if galaxyAddresses[galaxy][1] > newColumnValue:
            galaxyAddresses[galaxy][1] += 999999
    columnsAdded += 1

rowsAdded = 0
for row in rowsToAdd:
    newRowValue = row + (rowsAdded * 999999)
    for galaxy in galaxyAddresses:
        if galaxyAddresses[galaxy][0] > newRowValue:
            galaxyAddresses[galaxy][0] += 999999
    rowsAdded += 1

totalPathLengths = 0
while len(galaxiesList) > 1:
    workingGalaxy = galaxiesList.pop(0)
    for otherGalaxy in galaxiesList:
        rowDiff = galaxyAddresses[str(otherGalaxy)][0] - galaxyAddresses[str(workingGalaxy)][0]
        columnDiff = galaxyAddresses[str(otherGalaxy)][1] - galaxyAddresses[str(workingGalaxy)][1]
        pathLength = abs(rowDiff) + abs(columnDiff)
        totalPathLengths += pathLength

print(totalPathLengths)