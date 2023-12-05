import re

data = open('input.txt').read()
sections = data.split("\n\n")
seeds = []

for section in sections:
    sectionTitle = section.split(':')[0]
    maps = section.split(':')[1].replace('\n', ' ')
    mapValues = re.findall(r'\d+', maps)
    destinationRangeStart, sourceRangeStart, rangeLength = [], [], []

    if sectionTitle == 'seeds':
        for value in mapValues:
            seeds.append(int(value))
        print(seeds)

    else:
        for valIndex, value in enumerate(mapValues):
            if valIndex % 3 == 0:
                destinationRangeStart.append(int(value))
            elif (valIndex + 2) % 3 == 0:
                sourceRangeStart.append(int(value))
            elif (valIndex + 1) % 3 == 0:
                rangeLength.append(int(value))

        newSeeds = []

        for seed in seeds:
            mapped = False
            for sourceIndex, sourceVal in enumerate(sourceRangeStart):
                if seed >= sourceVal and seed < sourceVal + rangeLength[sourceIndex]:
                    newSeeds.append(seed + (destinationRangeStart[sourceIndex] - sourceVal))
                    mapped = True

            if not mapped:
                newSeeds.append(seed)

        seeds = newSeeds

smallestLocation = min(seeds)
print(smallestLocation)