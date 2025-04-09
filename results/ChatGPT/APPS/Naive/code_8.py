def min_draws_to_win(tiles):
    suits = {'m': [], 'p': [], 's': []}
    
    # Parse the input tiles into suits
    for tile in tiles:
        number = int(tile[0])
        suit = tile[1]
        suits[suit].append(number)
    
    # Check for existing mentsus
    for suit in suits:
        numbers = sorted(suits[suit])
        # Check for koutsu
        if len(set(numbers)) == 1:
            return 0  # Found a koutsu
        
        # Check for shuntsu
        for i in range(len(numbers) - 2):
            if numbers[i] + 1 == numbers[i + 1] and numbers[i + 1] + 1 == numbers[i + 2]:
                return 0  # Found a shuntsu

    # Check for possible shuntsus with one draw
    for suit in suits:
        numbers = sorted(suits[suit])
        if len(numbers) == 3:
            # Check for gaps in the sequence
            if (numbers[0] + 1 == numbers[1] and numbers[1] + 1 != numbers[2]) or \
               (numbers[0] != numbers[1] and numbers[1] + 1 == numbers[2]) or \
               (numbers[0] + 1 != numbers[1] and numbers[1] != numbers[2]):
                return 1  # Can form a shuntsu with one draw
        
        elif len(numbers) == 2:
            # Check if they can form a shuntsu with one draw
            if abs(numbers[0] - numbers[1]) == 1:
                return 1  # Can form a shuntsu with one draw
            if numbers[0] + 1 == numbers[1] - 1:
                return 1  # Can draw the missing middle tile
            
        elif len(numbers) == 1:
            # Only one tile, needs two more for a shuntsu
            return 2  # Need two more different tiles

    return 2  # If no mentsu can be formed

# Read input
tiles = input().split()
print(min_draws_to_win(tiles))