data = open('input.txt').read()
patterns = data.split("\n\n")

total = 0

for patternIndex, pattern in enumerate(patterns):
    patternLines = pattern.split('\n')
    length = len(patternLines)
    # check for horizontal reflection
    for lineIndex, line in enumerate(patternLines):
        if lineIndex > 0:
            if line == patternLines[lineIndex - 1]:
                reflectionFound = True
                lowerIndex = lineIndex - 1
                upperIndex = lineIndex
                while lowerIndex >= 0 and upperIndex < length:
                    if patternLines[lowerIndex] == patternLines[upperIndex]:
                        lowerIndex -= 1
                        upperIndex += 1
                    else:
                        reflectionFound = False
                        break
                if reflectionFound:
                    total += 100*lineIndex

    # check for vertical reflection
    width = len(patternLines[0])
    for columnIndex in range(width):
        if columnIndex > 0:
            column = [line[columnIndex] for line in patternLines]
            prevColumn = [line[columnIndex - 1] for line in patternLines]
            if column == prevColumn:
                reflectionFound = True
                lowerIndex = columnIndex - 1
                upperIndex = columnIndex
                while lowerIndex >= 0 and upperIndex < width:
                    upperColumn = [line[upperIndex] for line in patternLines]
                    lowerColumn = [line[lowerIndex] for line in patternLines]
                    if lowerColumn == upperColumn:
                        lowerIndex -= 1
                        upperIndex += 1
                    else:
                        reflectionFound = False
                        break
                if reflectionFound:
                    total += columnIndex

print(total)