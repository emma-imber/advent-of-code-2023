inputInLines = open('input.txt', 'r').readlines()

gamePowerSum = 0

for game in inputInLines:
    gameId = game.split(': ')[0].split(' ')[1]
    rounds = game.rstrip().split(': ')[1].split('; ')
    maxGameValues = {
        'red': 0,
        'green': 0,
        'blue': 0,
    }

    for round in rounds:
        roundDiceCounts = round.split(', ')

        for diceCount in roundDiceCounts:
            colour = diceCount.split(' ')[1]
            match colour:
                case 'red':
                    if int(diceCount.split(' ')[0]) > maxGameValues['red']:
                        maxGameValues['red'] = int(diceCount.split(' ')[0])
                case 'green':
                    if int(diceCount.split(' ')[0]) > maxGameValues['green']:
                        maxGameValues['green'] = int(diceCount.split(' ')[0])
                case 'blue':
                    if int(diceCount.split(' ')[0]) > maxGameValues['blue']:
                        maxGameValues['blue'] = int(diceCount.split(' ')[0])

    gamePowerSum += maxGameValues['red'] * maxGameValues['green'] * maxGameValues['blue']

print(gamePowerSum)