def minimum_draws(tiles):
    # Convert input to a list of tuples for easier processing
    tiles = [(int(t[0]), t[1]) for t in tiles]
    
    # Check for koutsu (triplet)
    count = {}
    for value, suit in tiles:
        count[(value, suit)] = count.get((value, suit), 0) + 1
    
    # If we have a triplet
    if any(c == 3 for c in count.values()):
        return 0
    
    # Check for shuntsu (sequence)
    suits = {'m': [], 'p': [], 's': []}
    for value, suit in tiles:
        suits[suit].append(value)
    
    # Sort the values for each suit
    for suit in suits:
        suits[suit].sort()
    
    # Function to check if we can form a shuntsu
    def can_form_shuntsu(values):
        for i in range(len(values) - 2):
            if values[i] + 1 == values[i + 1] and values[i + 1] + 1 == values[i + 2]:
                return True
        return False
    
    # If we can already form a shuntsu
    for suit in suits:
        if can_form_shuntsu(suits[suit]):
            return 0
    
    # Check if we can form a shuntsu by drawing one tile
    for suit in suits:
        if len(suits[suit]) == 2:
            if abs(suits[suit][0] - suits[suit][1]) == 1:
                return 1
            if suits[suit][0] == 1 or suits[suit][1] == 9:
                return 1
    
    # If we have two tiles of the same suit, we need one more tile
    for suit in suits:
        if len(suits[suit]) == 1:
            return 2
    
    return 2  # If no condition is satisfied, at least 2 more tiles are needed

# Read input
tiles = input().strip().split()
# Output the result
print(minimum_draws(tiles))