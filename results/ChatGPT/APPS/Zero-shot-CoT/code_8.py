def min_tiles_to_draw(tiles):
    from collections import Counter

    # Count occurrences of each tile
    counts = Counter(tiles)
    
    # Check for koutsu (triplet)
    for tile, count in counts.items():
        if count == 3:
            return 0  # Already has a koutsu

    # Check for shuntsu (sequence)
    suits = {'m': [], 'p': [], 's': []}
    for tile in tiles:
        number = int(tile[0])
        suit = tile[1]
        suits[suit].append(number)

    # Sort the numbers in each suit
    for suit in suits:
        suits[suit].sort()

    # Check for existing shuntsu
    for suit in suits:
        for i in range(len(suits[suit]) - 2):
            if suits[suit][i] + 1 == suits[suit][i + 1] and suits[suit][i] + 2 == suits[suit][i + 2]:
                return 0  # Already has a shuntsu

    # Check how many tiles are needed to form a shuntsu
    needed_tiles = 2  # Start with the maximum needed to form a shuntsu

    for suit in suits:
        for number in suits[suit]:
            # Check for the possibility of forming a shuntsu with one tile drawn
            if number - 1 in suits[suit] and number + 1 in suits[suit]:
                return 1  # Can form a shuntsu with one tile drawn
            if number - 1 not in suits[suit] and number + 1 not in suits[suit]:
                needed_tiles = min(needed_tiles, 2)  # Need two tiles to form a shuntsu
            else:
                needed_tiles = min(needed_tiles, 1)  # Need one tile to form a shuntsu

    return needed_tiles

# Input reading
tiles = input().strip().split()
print(min_tiles_to_draw(tiles))