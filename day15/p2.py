input = open('input.txt', 'r').read()
initSequence = input.split(',')

boxes = {}

for step in initSequence:
    operation = ''
    if '-' in step:
        label = step.split('-')[0]
        operation = 'remove'
    elif '=' in step:
        label = step.split('=')[0]
        operation = 'add'
        focalLength = step.split('=')[1]

    box = 0
    for char in label:
        box += ord(char)
        box = box * 17
        box = box % 256

    if operation == 'add':
        if str(box) in boxes:
            boxes[str(box)][label] = focalLength
        else:
            boxes[str(box)] = {label: focalLength}
    
    if operation == 'remove':
        if str(box) in boxes:
            if label in boxes[str(box)]:
                boxes[str(box)].pop(label)

totalFocusingPower = 0
for box in boxes:
    for lensNum, lens in enumerate(boxes[box].values()):
        focusingPower = (int(box) + 1)*(lensNum + 1)*int(lens)
        totalFocusingPower += focusingPower

print(totalFocusingPower)