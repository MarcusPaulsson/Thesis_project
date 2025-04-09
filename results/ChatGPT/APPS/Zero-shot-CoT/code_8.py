def min_tiles_to_draw(tiles):
    # Parse the tiles into a structured format
    hand = []
    for tile in tiles.split():
        number = int(tile[0])
        suit = tile[1]
        hand.append((number, suit))

    # Check for koutsu (triplet)
    counts = {}
    for num, suit in hand:
        counts[(num, suit)] = counts.get((num, suit), 0) + 1

    # If there's a koutsu, no need to draw
    if any(count == 3 for count in counts.values()):
        return 0

    # Check for shuntsu (sequence)
    suits = {'m': [], 'p': [], 's': []}
    for num, suit in hand:
        suits[suit].append(num)

    # Sort the numbers in each suit
    for suit in suits:
        suits[suit].sort()

    # Check for existing shuntsu
    for suit in suits:
        for i in range(len(suits[suit]) - 2):
            if suits[suit][i] + 1 == suits[suit][i + 1] and suits[suit][i] + 2 == suits[suit][i + 2]:
                return 0

    # Check how many extra tiles need to be drawn
    # We will check each suit and see if we can form a shuntsu with 1 additional tile
    for suit in suits:
        for num in suits[suit]:
            # Check if we can add a tile to form a shuntsu
            if (num - 1) not in suits[suit] and (num + 1) not in suits[suit]:
                if (num - 1) >= 1:
                    return 1  # Need to draw num-1
                if (num + 1) <= 9:
                    return 1  # Need to draw num+1

        # Check if we can form a shuntsu with two additional tiles
        if len(suits[suit]) == 2:
            if suits[suit][0] + 1 == suits[suit][1] - 1:
                return 2  # Need to draw the number in between

    # If none of the above conditions are met, we will need at least 2 tiles
    return 2

# Read input
tiles = input().strip()
# Get the minimum number of tiles to draw
result = min_tiles_to_draw(tiles)
# Print the result
print(result)