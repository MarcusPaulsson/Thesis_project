def min_draws(tiles):
    suits = {'m': [], 'p': [], 's': []}
    
    for tile in tiles:
        number = int(tile[0])
        suit = tile[1]
        suits[suit].append(number)
    
    # Check for koutsu
    for suit in suits.values():
        if len(suit) == 3 and len(set(suit)) == 1:
            return 0
    
    # Check for shuntsu
    for suit in suits.values():
        suit.sort()
        for i in range(len(suit) - 2):
            if suit[i] + 1 == suit[i + 1] and suit[i] + 2 == suit[i + 2]:
                return 0
    
    # Check for possible shuntsu with one draw
    for suit in suits.values():
        suit.sort()
        for number in suit:
            if number > 1 and number < 9:  # Can form shuntsu
                if (number - 1) not in suit or (number + 1) not in suit:
                    return 1
            elif number == 1:  # Can only add 2
                if (number + 1) not in suit:
                    return 1
            elif number == 9:  # Can only add 8
                if (number - 1) not in suit:
                    return 1
    
    # If no shuntsu or koutsu can be formed with one draw, need two draws
    return 2

# Input reading
tiles = input().split()
print(min_draws(tiles))