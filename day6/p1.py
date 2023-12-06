import re
data = open('input.txt').readlines()
times = re.findall(r'\d+', data[0])
distances = re.findall(r'\d+', data[1])
waysToWinProduct = 1

for index, time in enumerate(times):
    waysToWinRace = 0
    raceTime = int(time)
    for buttonTime in range(raceTime + 1):
        distance = (raceTime*buttonTime) - (buttonTime ** 2)
        if distance > int(distances[index]):
            waysToWinRace += 1
    waysToWinProduct = waysToWinProduct * waysToWinRace

print(waysToWinProduct)