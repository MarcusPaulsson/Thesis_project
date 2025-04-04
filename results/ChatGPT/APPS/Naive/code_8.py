def min_tiles_to_draw(tiles):
    suits = {'m': [], 'p': [], 's': []}
    
    for tile in tiles:
        number = int(tile[0])
        suit = tile[1]
        suits[suit].append(number)
    
    # Check for koutsu (triplet)
    for suit in suits:
        if suits[suit].count(suits[suit][0]) == 3:
            return 0
    
    # Check for shuntsu (sequence)
    for suit in suits:
        suit_numbers = sorted(suits[suit])
        if len(suit_numbers) >= 3:
            for i in range(len(suit_numbers) - 2):
                if suit_numbers[i + 1] == suit_numbers[i] + 1 and suit_numbers[i + 2] == suit_numbers[i] + 2:
                    return 0

    # Check for needed draws to form a shuntsu
    for suit in suits:
        if len(suits[suit]) == 2:
            missing_tiles = set([suits[suit][0] - 1, suits[suit][0], suits[suit][0] + 1,
                                 suits[suit][1] - 1, suits[suit][1], suits[suit][1] + 1])
            missing_tiles.discard(suits[suit][0])
            missing_tiles.discard(suits[suit][1])
            if any(1 <= tile <= 9 for tile in missing_tiles):
                return 1
    
    # If we only have one tile of one suit, we need two draws to form a shuntsu
    for suit in suits:
        if len(suits[suit]) == 1:
            return 2
    
    return 3  # If we have no matching tiles at all, we need at least 3 draws

# Read input
tiles = input().strip().split()
print(min_tiles_to_draw(tiles))