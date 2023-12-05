import re

lines = open('input.txt').readlines()
length = len(lines)
width = len(lines[0].rstrip())
partsNumberTotal = 0
validPartNumberIndexes = {}
#have to use a unique id to handle case where two parts numbers on a gear
# have the same value, and using the set removes one number
uniqueId = 1

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
                    validPartNumberIndexes[str(lineIndex) + ' ' + str(num.start()+ charIndex)] = num.group() + ' ' + str(uniqueId)
        
        if isValidPartNumber:
            partsNumberTotal += int(num.group())
    
    uniqueId += 1

print(validPartNumberIndexes)

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

            print(setOfAdjacentPartNumbers)
            
            if len(setOfAdjacentPartNumbers) == 2:
                partNums = list(setOfAdjacentPartNumbers)
                #here we remove the unique id
                gearRatio = int(partNums[0].split(' ')[0]) * int(partNums[1].split(' ')[0])
                totalOfGearRatios += gearRatio
            
print("Total of gear ratios: " + str(totalOfGearRatios))        