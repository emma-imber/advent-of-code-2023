lines = open('input.txt', 'r').readlines()
pipeSystem = []
graph = {}
sLocation = ''

# build pipeSystem
for line in lines:
    pipeSystem.append(list(line.strip()))

maxYCoord = len(pipeSystem) - 1
maxXCoord = len(pipeSystem[0]) -1

pipeCharacters = {
    '|': ['up', 'down'],
    '-': ['left', 'right'],
    'L': ['up', 'right'],
    'J': ['up', 'left'],
    'F': ['down', 'right'],
    '7': ['down', 'left'],
    # I manually checked what the valid options for S were because life is too short
    'S': ['up', 'down']
}

coordChanges = {
    'up': [0, -1],
    'down': [0, 1],
    'left': [-1, 0],
    'right': [1, 0]
}

# build graph of nodes and their connections
for yCoord, row in enumerate(pipeSystem):
    for xCoord, character in enumerate(row):
        adjacentCoords = []
        if character in pipeCharacters:
            directions = pipeCharacters[character]
            for direction in directions:
                adjacentCoords.append(str(xCoord + coordChanges[direction][0]) + ' ' + str(yCoord + coordChanges[direction][1]))
            graph[str(xCoord) + ' ' + str(yCoord)] = adjacentCoords
        if character == 'S':
            sLocation = str(xCoord) + ' ' + str(yCoord)

visited = {}

def breadthFirstSearch(visited, graph, node):  
    visited[node] = 0
    queue = [[sLocation, 0]]

    while queue:
        currentNode, currentDist = queue.pop(0)
        if currentNode in graph:
            for neighbour in graph[currentNode]:
                if neighbour not in visited:
                    if neighbour in graph:
                        visited[neighbour] = currentDist + 1
                        queue.append([neighbour, currentDist + 1])
        
breadthFirstSearch(visited, graph, sLocation)

print(max(visited.values()))

# part 2

cleanedPipeSystem = []
# reassign pipes that aren't in the loop
for yCoord, row in enumerate(pipeSystem):
    cleanedRow = []
    for xCoord, character in enumerate(row):
        if str(xCoord) + ' ' + str(yCoord) not in visited:
            cleanedRow.append('.')
        else:
            cleanedRow.append(character)
    cleanedPipeSystem.append(cleanedRow)

outside = []
for yCoord, row in enumerate(cleanedPipeSystem):
    inPipe = False
    prevCorner = ''
    for xCoord, character in enumerate(row):
        if character == '|' or character == 'S':
            # means we've crossed
            inPipe = not inPipe
        # if you see an L then a J, you're not crossing
        # but if you see an L then a 7, you are
        elif character == 'L':
            prevCorner = 'L'
        elif character == 'F':
            prevCorner = 'F'
        elif character == 'J':
            if prevCorner == 'F':
                inPipe = not inPipe
        elif character == '7':
            if prevCorner == 'L':
                inPipe = not inPipe
        if not inPipe:
            outside.append(str(xCoord) + ' ' + str(yCoord))

totalInside = 0   
for yCoord, row in enumerate(cleanedPipeSystem):
    for xCoord, character in enumerate(row):
        isInside = True
        if str(xCoord) + ' ' + str(yCoord) in visited:
            isInside = False
        elif str(xCoord) + ' ' + str(yCoord) in outside:
            isInside = False
        if isInside:
            totalInside += 1

print(totalInside)