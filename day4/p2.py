lines = open('input.txt').readlines()
totalCardScore = 0
timesToPlayEachCard = {}

for lineIndex, line in enumerate(lines):
    timesToPlayEachCard[lineIndex] = 1

for lineIndex, line in enumerate(lines):
    cardNumbers = line.rstrip().split(': ')[1].split(' | ')
    winningNumbers = cardNumbers[0].split(' ')
    numbersWeHave = cardNumbers[1].split(' ')
    cleanedWinningNumbers = [item for item in winningNumbers if item != '']
    cleanedNumbersWeHave = [item for item in numbersWeHave if item != '']
    
    for i in range(timesToPlayEachCard[lineIndex]):
        numberOfWins = 0
        for number in cleanedNumbersWeHave:
            if number in cleanedWinningNumbers:
                numberOfWins += 1

        for x in range(numberOfWins):
            timesToPlayEachCard[lineIndex + x + 1] += 1

totalCards = 0
for card in timesToPlayEachCard:
    totalCards += timesToPlayEachCard[card]

print(totalCards)