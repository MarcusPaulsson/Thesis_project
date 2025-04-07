def min_draws_to_win(tiles):
    # Convert tiles to a more manageable format
    counts = {}
    suits = {'m': [], 'p': [], 's': []}
    
    for tile in tiles:
        number = int(tile[0])
        suit = tile[1]
        counts[tile] = counts.get(tile, 0) + 1
        suits[suit].append(number)
    
    # Check for koutsu (triplet)
    if any(count == 3 for count in counts.values()):
        return 0  # Already have a koutsu

    # Sort numbers for each suit
    for suit in suits:
        suits[suit].sort()

    # Check for existing shuntsu
    for suit in suits:
        for i in range(len(suits[suit]) - 2):
            if suits[suit][i] + 1 == suits[suit][i + 1] and suits[suit][i + 1] + 1 == suits[suit][i + 2]:
                return 0  # Already have a shuntsu

    # Check if we can form a shuntsu by drawing 1 tile
    for suit in suits:
        for number in suits[suit]:
            # Check if we can complete a sequence
            if number - 1 >= 1 and (number - 1) not in suits[suit]:  # Need number - 1
                return 1
            if number + 1 <= 9 and (number + 1) not in suits[suit]:  # Need number + 1
                return 1

    # No tile can create a shuntsu, we must draw 2 tiles
    return 2

tiles = input().split()
print(min_draws_to_win(tiles))