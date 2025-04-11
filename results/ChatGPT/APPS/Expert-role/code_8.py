def min_tiles_to_draw(tiles):
    # Parse the input tiles
    hand = [(int(tile[0]), tile[1]) for tile in tiles]
    
    # Check for koutsu (triplet)
    counts = {}
    for num, suit in hand:
        if (num, suit) in counts:
            counts[(num, suit)] += 1
        else:
            counts[(num, suit)] = 1
    
    # If there's a koutsu
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
    
    # Check how many tiles are needed to form a shuntsu
    min_needed = float('inf')
    
    for suit in suits:
        for num in suits[suit]:
            # Check for possible shuntsu formations
            needed = 0
            if num - 1 not in suits[suit]:
                needed += 1
            if num + 1 not in suits[suit]:
                needed += 1
            
            # If we need 2 tiles to form a shuntsu
            if needed == 2:
                min_needed = min(min_needed, 2)
            # If we need 1 tile to form a shuntsu
            elif needed == 1:
                min_needed = min(min_needed, 1)
    
    return min_needed if min_needed != float('inf') else 2

# Read input
tiles = input().strip().split()
# Output the result
print(min_tiles_to_draw(tiles))