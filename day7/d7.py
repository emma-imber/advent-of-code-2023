from collections import Counter
from functools import cmp_to_key

cardHierarchy = {
    #port part 2 change value of J
    'A': 13,
    'K': 12,
    'Q': 11,
    'J': 10,
    'T': 9,
    '9': 8,
    '8': 7,
    '7': 6,
    '6': 5,
    '5': 4,
    '4': 3,
    '3': 2,
    '2': 1
}

def identifyHand(handList):
    cardCount = Counter(handList)
    # for part 2, add these lines instead of line 22
    '''
    initialCardCount = Counter(handList)
    mostCommonCard = initialCardCount.most_common(1)[0][0]
    if mostCommonCard == 'J' and len(initialCardCount) > 1:
        mostCommonCard = initialCardCount.most_common(2)[1][0]
    jokersReplacedList = [card.replace('J', mostCommonCard) for card in handList]
    cardCount = Counter(jokersReplacedList)
    '''

    if len(cardCount) == 1:
        # Five of a kind
        return 7
    elif len(cardCount) == 2:
        if cardCount.most_common(1)[0][1] == 4:
            # Four of a kind
            return 6
        elif cardCount.most_common(1)[0][1] == 3:
            # Full house
            return 5
    elif len(cardCount) == 3:
        if cardCount.most_common(1)[0][1] == 3:
            # Three of a kind
            return 4
        elif cardCount.most_common(1)[0][1] == 2:
            # Two pair
            return 3
    elif len(cardCount) == 4:
        # One pair
        return 2
    else:
        # High card
        return 1

def compareHands(hand1, hand2):
    hand1List = [*hand1]
    hand2List = [*hand2]
    if identifyHand(hand1List) < identifyHand(hand2List):
        return -1
    elif identifyHand(hand1List) > identifyHand(hand2List):
        return 1
    else:
        result = 0
        for index, card in enumerate(hand1List):
            if cardHierarchy[card] > cardHierarchy[hand2List[index]]:
                result = 1
                break
            elif cardHierarchy[card] < cardHierarchy[hand2List[index]]:
                result = -1
                break
        return result

bidDictionary = {}
handList = []
inputInLines = open('input.txt', 'r').readlines()

for line in inputInLines:
    hand = line.rstrip().split(" ")[0]
    bid = line.rstrip().split(" ")[1]
    bidDictionary[hand] = int(bid)
    handList.append(hand)

handList.sort(key=cmp_to_key(compareHands))

total = 0

for index, hand in enumerate(handList):
    rank = index + 1
    product = rank * bidDictionary[hand]
    total += product

print(total)