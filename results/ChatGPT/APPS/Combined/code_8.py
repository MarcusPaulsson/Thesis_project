def minimum_draws(tiles):
    # Count occurrences of tiles using a dictionary
    counts = {}
    for tile in tiles:
        num = int(tile[0])
        suit = tile[1]
        counts[(num, suit)] = counts.get((num, suit), 0) + 1
    
    # Check for koutsu (triplet)
    if any(count >= 3 for count in counts.values()):
        return 0  # No draws needed if we have a triplet
    
    # Organize tiles by suit
    suits = {'m': [], 'p': [], 's': []}
    for (num, suit), count in counts.items():
        suits[suit].append(num)
    
    # Check for shuntsu (sequences) in each suit
    for suit, numbers in suits.items():
        numbers.sort()
        n = len(numbers)
        
        # Check for existing shuntsu
        for i in range(n - 2):
            if numbers[i + 2] - numbers[i] == 2 and numbers[i + 1] - numbers[i] == 1:
                return 0  # No draws needed if we have a sequence

        # Check for draws needed to form a shuntsu
        for number in numbers:
            needed_tiles = [(number - 1, suit), (number + 1, suit)]
            if all(tile not in counts for tile in needed_tiles):
                return 2  # Need 2 draws
            elif any(tile not in counts for tile in needed_tiles):
                return 1  # Need 1 draw

    return 2  # If no koutsu or shuntsu can be formed, need 2 draws

# Read input
tiles = input().strip().split()
# Get the result and print
result = minimum_draws(tiles)
print(result)