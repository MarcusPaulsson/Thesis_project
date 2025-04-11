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
    
    # If there's a koutsu, return 0
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
    
    # Check for possible shuntsu with one draw
    for suit in suits:
        for num in suits[suit]:
            if num - 1 >= 1 and (num - 1) not in suits[suit]:  # Check for num-1
                if num + 1 not in suits[suit]:  # Check for num+1
                    return 1
            if num + 1 <= 9 and (num + 1) not in suits[suit]:  # Check for num+1
                if num - 1 not in suits[suit]:  # Check for num-1
                    return 1
    
    # If no shuntsu can be formed with one draw, return 2
    return 2

# Read input
tiles = input().strip().split()
# Output the result
print(min_tiles_to_draw(tiles))