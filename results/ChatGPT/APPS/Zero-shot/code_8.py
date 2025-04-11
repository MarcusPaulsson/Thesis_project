def min_draws(tiles):
    from collections import Counter

    # Parse the input tiles
    counts = Counter(tiles)
    
    # Check for koutsu (triplet)
    for tile, count in counts.items():
        if count >= 3:
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
    for suit, numbers in suits.items():
        if len(numbers) >= 3:
            for i in range(len(numbers) - 2):
                if numbers[i + 1] == numbers[i] + 1 and numbers[i + 2] == numbers[i] + 2:
                    return 0  # Already has a shuntsu

    # Check how many draws are needed
    needed = 2  # Start with the maximum needed draws

    for suit, numbers in suits.items():
        if len(numbers) == 2:
            # Check if we can form a shuntsu with one draw
            if (numbers[0] + 1 == numbers[1]) or (numbers[0] + 2 == numbers[1]):
                needed = min(needed, 1)
            else:
                needed = min(needed, 2)
        elif len(numbers) == 1:
            # Only one tile, need two draws to form a shuntsu
            needed = min(needed, 2)

    return needed

# Read input
tiles = input().strip().split()
# Output the result
print(min_draws(tiles))