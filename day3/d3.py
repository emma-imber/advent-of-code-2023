import re

lines = open('input.txt').readlines()
length = len(lines)
width = len(lines[0].rstrip())
partsNumberTotal = 0
validPartNumberIndexes = {}

for lineIndex, line in enumerate(lines):
    partNumbers = re.finditer(r'\d+', line)
    for num in partNumbers:
        adjacentValues = []
        if lineIndex > 0:
            adjacentValues.append(lines[lineIndex-1][num.start()])
            adjacentValues.append(lines[lineIndex-1][num.end()-1])
            if num.end() - num.start() > 2:
                adjacentValues.append(lines[lineIndex-1][num.start()+1])
        if lineIndex < length - 1:
            adjacentValues.append(lines[lineIndex+1][num.start()])
            adjacentValues.append(lines[lineIndex+1][num.end()-1])
            if num.end() - num.start() > 2:
                adjacentValues.append(lines[lineIndex+1][num.start()+1])
        if num.start() > 0:
            adjacentValues.append(lines[lineIndex][num.start()-1])
            if lineIndex > 0:
                adjacentValues.append(lines[lineIndex-1][num.start()-1])
            if lineIndex < length - 1:
                adjacentValues.append(lines[lineIndex+1][num.start()-1])
        if num.end() < width:
            adjacentValues.append(lines[lineIndex][num.end()])
            if lineIndex > 0:
                adjacentValues.append(lines[lineIndex-1][num.end()])
            if lineIndex < length - 1:
                adjacentValues.append(lines[lineIndex+1][num.end()])
        
        isValidPartNumber = False
        
        for value in adjacentValues:
            if value != '.' and not value.isdigit():
                isValidPartNumber = True
                for charIndex, char in enumerate(num.group()):
                    validPartNumberIndexes[str(lineIndex) + ' ' + str(num.start()+ charIndex)] = int(num.group())
        
        if isValidPartNumber:
            partsNumberTotal += int(num.group())


print("Part number total: " + str(partsNumberTotal))

totalOfGearRatios = 0
for part2LineIndex, part2Line in enumerate(lines):
    for part2CharIndex, part2Char in enumerate(part2Line):
        if part2Char == '*':
            adjacentPartNumbers = []
            adjacentPositions = [
                str(part2LineIndex - 1) + ' ' + str(part2CharIndex - 1),
                str(part2LineIndex - 1) + ' ' + str(part2CharIndex),
                str(part2LineIndex - 1) + ' ' + str(part2CharIndex + 1),
                str(part2LineIndex) + ' ' + str(part2CharIndex - 1),
                str(part2LineIndex) + ' ' + str(part2CharIndex + 1),
                str(part2LineIndex + 1) + ' ' + str(part2CharIndex - 1),
                str(part2LineIndex + 1) + ' ' + str(part2CharIndex),
                str(part2LineIndex + 1) + ' ' + str(part2CharIndex + 1)
            ]

            for position in adjacentPositions:
                if position in validPartNumberIndexes:
                    adjacentPartNumbers.append(validPartNumberIndexes[position])
            
            setOfAdjacentPartNumbers = set(adjacentPartNumbers)
            
            if len(setOfAdjacentPartNumbers) == 2:
                partNums = list(setOfAdjacentPartNumbers)
                gearRatio = partNums[0] * partNums[1]
                totalOfGearRatios += gearRatio
            
#doesn't work, need to troubleshoot

print("Total of gear ratios: " + str(totalOfGearRatios))        