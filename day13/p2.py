data = open('input.txt').read()
patterns = data.split("\n\n")

def calculateDifference(list1, list2):
    totalDiff = 0
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            totalDiff += 1
    return totalDiff

total = 0

for patternIndex, pattern in enumerate(patterns):
    patternLines = pattern.split('\n')
    length = len(patternLines)
    # check for horizontal reflection
    for lineIndex, line in enumerate(patternLines):
        if lineIndex > 0:
            totalDiffForIndex = 0
            lowerIndex = lineIndex - 1
            upperIndex = lineIndex
            while lowerIndex >= 0 and upperIndex < length:
                totalDiffForIndex += calculateDifference(patternLines[lowerIndex], patternLines[upperIndex])
                lowerIndex -= 1
                upperIndex += 1
            if totalDiffForIndex == 1:
                total += 100*lineIndex

    # check for vertical reflection
    width = len(patternLines[0])
    for columnIndex in range(width):
        if columnIndex > 0:
            totalDiffForIndex = 0
            column = [line[columnIndex] for line in patternLines]
            prevColumn = [line[columnIndex - 1] for line in patternLines]
            reflectionFound = True
            lowerIndex = columnIndex - 1
            upperIndex = columnIndex
            while lowerIndex >= 0 and upperIndex < width:
                upperColumn = [line[upperIndex] for line in patternLines]
                lowerColumn = [line[lowerIndex] for line in patternLines]
                totalDiffForIndex += calculateDifference(lowerColumn, upperColumn)
                lowerIndex -= 1
                upperIndex += 1
            if totalDiffForIndex == 1:
                total += columnIndex

print(total)