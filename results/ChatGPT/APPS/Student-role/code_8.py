def min_draws_needed(tiles):
    suits = {'m': [], 'p': [], 's': []}
    
    # Parse the input tiles
    for tile in tiles:
        number = int(tile[0])
        suit = tile[1]
        suits[suit].append(number)

    # Check for koutsu (triplet)
    for suit in suits.values():
        if len(suit) >= 3 and len(set(suit)) == 1:
            return 0  # Already has a koutsu

    # Check for shuntsu (sequence)
    for suit in suits.values():
        suit.sort()
        for i in range(len(suit) - 1):
            if suit[i] + 1 == suit[i + 1]:
                # Found a sequence, no need to draw
                return 0
            if i < len(suit) - 2 and suit[i] + 2 == suit[i + 2]:
                # Found a gap that can be filled with one tile
                return 1
    
    # Check for missing tiles to create a shuntsu
    for suit in suits.values():
        if len(suit) == 2:
            # Check if we can fill the gap for a shuntsu
            if abs(suit[0] - suit[1]) == 2:
                return 1  # Need to draw one tile to complete the sequence

    return 2  # Otherwise, we need to draw two tiles

# Input reading
tiles = input().strip().split()
print(min_draws_needed(tiles))