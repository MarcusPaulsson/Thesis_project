def min_tiles_to_draw(tiles):
    # Parse the input tiles
    hand = [tile for tile in tiles.split()]
    
    # Count occurrences of each tile
    count = {}
    for tile in hand:
        count[tile] = count.get(tile, 0) + 1
    
    # Check for koutsu (triplet)
    for tile, cnt in count.items():
        if cnt == 3:
            return 0  # Already has a koutsu
    
    # Check for shuntsu (sequence)
    suits = {'m': [], 'p': [], 's': []}
    for tile in hand:
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
    
    # Check how many tiles need to be drawn for shuntsu
    needed = 2  # Maximum needed is 2 tiles to form a shuntsu
    for suit in suits:
        for number in suits[suit]:
            # Check for possible shuntsu formations
            if number - 1 in suits[suit] and number + 1 in suits[suit]:
                return 0  # Already can form a shuntsu
            if number - 1 not in suits[suit] and number + 1 not in suits[suit]:
                needed = min(needed, 2)  # Need 2 tiles
            else:
                needed = min(needed, 1)  # Need 1 tile
    
    return needed

# Read input
tiles = input().strip()
# Output the result
print(min_tiles_to_draw(tiles))