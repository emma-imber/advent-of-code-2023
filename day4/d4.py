lines = open('input.txt').readlines()
totalCardScore = 0

for line in lines:
    cardNumbers = line.rstrip().split(': ')[1].split(' | ')
    winningNumbers = cardNumbers[0].split(' ')
    numbersWeHave = cardNumbers[1].split(' ')
    cleanedWinningNumbers = [item for item in winningNumbers if item != '']
    cleanedNumbersWeHave = [item for item in numbersWeHave if item != '']

    print(cleanedWinningNumbers)
    print(cleanedNumbersWeHave)
    
    numberOfWins = 0
    for number in cleanedNumbersWeHave:
        if number in cleanedWinningNumbers:
            numberOfWins += 1
    
    cardScore = 0
    if numberOfWins != 0:
        cardScore = pow(2, numberOfWins - 1)
    
    totalCardScore += cardScore

print(totalCardScore)