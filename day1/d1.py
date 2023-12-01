def replaceAll(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text

numberReplacements = {
    'one': 'o1e',
    'two': 't2o',
    'three': 't3e',
    'four': 'f4r',
    'five': 'f5e',
    'six': 's6x',
    'seven': 's7n',
    'eight': 'e8t',
    'nine': 'n9e'
}

inputInLines = open('input.txt', 'r').readlines()
totalOfCalibrationValues = 0
for line in inputInLines:
    # comment out the line below to solve part 1, reenable it to solve part 2
    line = replaceAll(line, numberReplacements)
    lineIntegers = []
    for character in line:
        try:
            lineIntegers.append(int(character))
        except Exception:
            pass
    calibrationValue = int(str(lineIntegers[0]) + str(lineIntegers[-1]))
    totalOfCalibrationValues += calibrationValue

print(totalOfCalibrationValues)