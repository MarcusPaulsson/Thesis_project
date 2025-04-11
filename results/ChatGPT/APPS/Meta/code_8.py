def min_tiles_to_draw(tiles):
    suits = {'m': [], 'p': [], 's': []}
    
    # Parse the input tiles and categorize them by suit
    for tile in tiles:
        number = int(tile[0])
        suit = tile[1]
        suits[suit].append(number)
    
    # Check for koutsu (triplet)
    for suit in suits.values():
        if len(suit) == 3 and suit[0] == suit[1] == suit[2]:
            return 0  # Already has a koutsu
    
    # Check for shuntsu (sequence)
    for suit in suits.values():
        if len(suit) >= 3:
            suit.sort()
            for i in range(len(suit) - 2):
                if suit[i] + 1 == suit[i + 1] and suit[i + 1] + 1 == suit[i + 2]:
                    return 0  # Already has a shuntsu
    
    # Check for potential shuntsu with one draw
    for suit in suits.values():
        if len(suit) == 2:
            # Check if we can form a shuntsu by drawing one tile
            if (suit[0] + 1 == suit[1] or suit[0] + 2 == suit[1] or suit[1] + 1 == suit[0] or suit[1] + 2 == suit[0]):
                return 1  # Can form a shuntsu with one draw
    
    # Check for potential shuntsu with two draws
    for suit in suits.values():
        if len(suit) == 1:
            # If we have one tile, we need two more to form a shuntsu
            if suit[0] > 1 and suit[0] < 9:
                return 2  # Need two draws to form a shuntsu
            else:
                return 2  # Need two draws to form a shuntsu (1 or 9 case)
    
    return 2  # If we have no tiles or all are different, we need two draws

# Read input
tiles = input().strip().split()
# Output the result
print(min_tiles_to_draw(tiles))