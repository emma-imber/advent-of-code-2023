lines = open('input.txt', 'r').readlines()

def isAllZeros(sequenceOfDifferences):
    allZeros = True
    for diff in sequenceOfDifferences:
        if diff != 0:
            allZeros = False
    return allZeros

totalOfPredictedNewVals = 0
totalOfPredictedHistoricalVals = 0
for line in lines:
    sequences = []
    sequences.append([int(x) for x in line.rstrip().split(' ')])
    numOfDiffSequences = 0
    reachedAllZeros = False

    # work out diff sequences until they contain all zeros
    while reachedAllZeros == False:
        diffSequence = []
        for index, value in enumerate(sequences[numOfDiffSequences]):
            if index == 0:
                continue
            else:
                diffSequence.append(sequences[numOfDiffSequences][index] - sequences[numOfDiffSequences][index - 1])
        
        sequences.append(diffSequence)
        numOfDiffSequences += 1
        reachedAllZeros = isAllZeros(diffSequence)

    # work back up to predict new value and historical value
    for i in range(numOfDiffSequences, -1, -1):
        if i == numOfDiffSequences:
            sequences[i].append(0)
            sequences[i].insert(0, 0)
        else:
            newValue = sequences[i][-1] + sequences[i + 1][-1]
            newHistoricalValue = sequences[i][0] - sequences[i + 1][0]
            sequences[i].append(newValue)
            sequences[i].insert(0, newHistoricalValue)

    totalOfPredictedNewVals += sequences[0][-1]
    totalOfPredictedHistoricalVals += sequences[0][0]

print(totalOfPredictedNewVals)
print(totalOfPredictedHistoricalVals)