import re
input = open('input.txt', 'r').readlines()

def findGroupSizes(springString):
    springString += '.'
    inGroup = False
    currentGroup = ''
    groups = []
    groupSizes = []
    for char in springString:
        if char == '#':
            if inGroup:
                currentGroup += '#'
            else:
                inGroup = True
                currentGroup = '#'
        else:
            if inGroup:
                groups.append(currentGroup)
                currentGroup = ''
                inGroup = False

    for group in groups:
        groupSizes.append(str(len(group)))

    return groupSizes

possibleArrangements = 0
for line in input:
    record = list(line.split(' ')[0])
    groupSizes = line.strip().split(' ')[1].split(',')
    stringsToTest = []
    for char in record:
        if char == '?':
            if len(stringsToTest) == 0:
                stringsToTest.append('.')
                stringsToTest.append('#')
            else:
                stringsCopy1 = []
                stringsCopy2 = []
                for string in stringsToTest:
                    stringsCopy1.append(string + '.')
                for string in stringsToTest:
                    stringsCopy2.append(string + '#')
                stringsToTest = stringsCopy1 + stringsCopy2
        else:
            if len(stringsToTest) == 0:
                stringsToTest.append(char)
            else:
                newStrings = []
                for string in stringsToTest:
                    newString = string + char
                    newStrings.append(newString)
                stringsToTest = newStrings
    
    potentialMatches = 0
    for string in stringsToTest:
        if findGroupSizes(string) == groupSizes:
            potentialMatches += 1

    possibleArrangements += potentialMatches

print(possibleArrangements)