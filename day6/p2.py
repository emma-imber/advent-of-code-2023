import re
data = open('input.txt').readlines()
time = re.findall(r'\d+', data[0])
intTime = int(''.join(time))
distance = re.findall(r'\d+', data[1])
intDistance = int(''.join(distance))

waysToWinRace = 0
for buttonTime in range(intTime + 1):
    distance = (intTime*buttonTime) - (buttonTime ** 2)
    if distance > int(intDistance):
        waysToWinRace += 1

print(waysToWinRace)