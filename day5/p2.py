import re
data = open('input.txt').read()
sections = data.split("\n\n")
seeds = sections[0].split(':')[1].replace('\n', ' ')
seeds = re.findall(r'\d+', seeds)
sections.reverse()
startLocation = 0
seedFound = False
interval = 5000

seedStarts, seedRanges = [], []
for index, value in enumerate(seeds):
    if index % 2 == 0:
        seedStarts.append(int(value))
    elif (index + 1) % 2 == 0:
        seedRanges.append(int(value))

def isValidSeed(potentialSeed):
    validSeed = False
    for startIndex, startVal in enumerate(seedStarts):
        if (potentialSeed >= startVal) and potentialSeed < (startVal + seedRanges[startIndex]):
            validSeed = True
    return validSeed

while seedFound == False:
    print(startLocation)
    workingLocation = startLocation
    for section in sections:
        sectionTitle = section.split(':')[0]
        maps = section.split(':')[1].replace('\n', ' ')
        mapValues = re.findall(r'\d+', maps)
        destinationRangeStart, sourceRangeStart, rangeLength = [], [], []

        if sectionTitle == 'seeds':
            if isValidSeed(workingLocation) and interval == 5000:
                startLocation -= 5000
                workingLocation -= 5000
                interval = 1
            elif isValidSeed(workingLocation) and interval == 1:
                seedFound = True
                print(startLocation)

        else:
            for valIndex, value in enumerate(mapValues):
                if valIndex % 3 == 0:
                    destinationRangeStart.append(int(value))
                elif (valIndex + 2) % 3 == 0:
                    sourceRangeStart.append(int(value))
                elif (valIndex + 1) % 3 == 0:
                    rangeLength.append(int(value))

            mapped = False
            for destinationIndex, destinationVal in enumerate(destinationRangeStart):
                if workingLocation >= destinationVal and workingLocation < destinationVal + rangeLength[destinationIndex]:
                    newLocation = workingLocation - (destinationVal - sourceRangeStart[destinationIndex])
                    mapped = True
            if mapped:
                workingLocation = newLocation    
    # use a bigger interval to get the range via brute force, and then dialled in
    startLocation += interval