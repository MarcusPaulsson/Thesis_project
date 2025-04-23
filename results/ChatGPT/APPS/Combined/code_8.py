def min_tiles_to_draw(tiles):
    from collections import Counter

    # Count occurrences of each tile
    counts = Counter(tiles)

    # Check for koutsu (triplet)
    if any(count >= 3 for count in counts.values()):
        return 0  # Already has a koutsu

    # Organize tiles by suit
    suits = {'m': [], 'p': [], 's': []}
    for tile in tiles:
        number = int(tile[0])
        suit = tile[1]
        suits[suit].append(number)

    # Sort the numbers in each suit
    for suit in suits:
        suits[suit].sort()

    # Check for existing shuntsu (sequence)
    for numbers in suits.values():
        if any(numbers[i] + 1 == numbers[i + 1] and numbers[i] + 2 == numbers[i + 2] for i in range(len(numbers) - 2)):
            return 0  # Already has a shuntsu

    # Check for possible shuntsu with one draw
    for numbers in suits.values():
        for i in range(len(numbers)):
            # Check for completing a sequence
            if (numbers[i] - 1) not in numbers or (numbers[i] + 1) not in numbers:
                return 1  # Can complete a shuntsu with one draw

            # Check for gaps in the sequence
            if i > 0 and numbers[i] - numbers[i - 1] > 1:
                return 1  # Can draw a tile to complete a shuntsu

    # If no mentsu can be formed with one draw, it requires two draws
    return 2

# Read input
tiles = input().strip().split()
# Output the result
print(min_tiles_to_draw(tiles))