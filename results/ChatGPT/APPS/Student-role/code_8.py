def min_tiles_to_draw(tiles):
    suits = {'m': [], 'p': [], 's': []}
    
    # Parse the tiles into suits
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
            suit = sorted(suit)
            for i in range(len(suit) - 2):
                if suit[i] + 1 == suit[i + 1] and suit[i + 1] + 1 == suit[i + 2]:
                    return 0  # Already has a shuntsu
    
    # Check for possible shuntsu with one draw
    for suit in suits.values():
        if len(suit) == 2:
            # Check if we can form a shuntsu by drawing one tile
            min_tile = min(suit)
            max_tile = max(suit)
            if (min_tile + 1 == max_tile) or (max_tile - 1 == min_tile):
                return 1  # Can form a shuntsu with one draw
            if (min_tile + 2 == max_tile):
                return 1  # Can form a shuntsu with one draw
            if (min_tile + 1 not in suit) or (max_tile - 1 not in suit):
                return 1  # Can draw to complete a shuntsu
    
    # Check for possible shuntsu with two draws
    for suit in suits.values():
        if len(suit) == 1:
            # Need two draws to form a shuntsu
            number = suit[0]
            if number > 1 and number < 9:
                return 2  # Can draw two tiles to form a shuntsu
            elif number == 1:
                return 2  # Need to draw 2 and 3
            elif number == 9:
                return 2  # Need to draw 7 and 8
    
    return 2  # If all else fails, need two draws

# Input reading
tiles = input().strip().split()
print(min_tiles_to_draw(tiles))