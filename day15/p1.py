input = open('input.txt', 'r').read()
initSequence = input.split(',')

hashTotal = 0
for step in initSequence:
    hash = 0
    for char in step:
        hash += ord(char)
        hash = hash * 17
        hash = hash % 256
    hashTotal += hash

print(hashTotal)