inputInLines = open('input.txt', 'r').readlines()

possibleGameIdSum = 0

for game in inputInLines:
    gameId = game.split(': ')[0].split(' ')[1]
    rounds = game.rstrip().split(': ')[1].split('; ')
    gameIsPossible = True

    for round in rounds:
        roundIsPossible = True
        roundDiceCounts = round.split(', ')

        for diceCount in roundDiceCounts:
            colour = diceCount.split(' ')[1]
            match colour:
                case 'red':
                    if int(diceCount.split(' ')[0]) > 12:
                        roundIsPossible = False
                case 'green':
                    if int(diceCount.split(' ')[0]) > 13:
                        roundIsPossible = False
                case 'blue':
                    if int(diceCount.split(' ')[0]) > 14:
                        roundIsPossible = False
        
        if roundIsPossible == False:
            gameIsPossible = False
    
    if gameIsPossible:
        possibleGameIdSum += int(gameId)

print(possibleGameIdSum)