def min_tiles_to_draw(tiles):
    from collections import defaultdict

    # Parse the input tiles
    hand = tiles.split()
    counts = defaultdict(int)
    suits = {'m': [], 'p': [], 's': []}

    for tile in hand:
        num = int(tile[0])
        suit = tile[1]
        counts[tile] += 1
        suits[suit].append(num)

    # Check for koutsu (triplet)
    if any(count == 3 for count in counts.values()):
        return 0  # Already has a koutsu

    # Check for shuntsu (sequence)
    for suit, numbers in suits.items():
        unique_numbers = sorted(set(numbers))
        for i in range(len(unique_numbers) - 2):
            if unique_numbers[i] + 1 == unique_numbers[i + 1] and unique_numbers[i] + 2 == unique_numbers[i + 2]:
                return 0  # Already has a shuntsu

    # If no mentsu, check how many tiles are needed
    needed = 2  # Start with the worst case (need 2 tiles)

    for suit, numbers in suits.items():
        unique_numbers = sorted(set(numbers))
        
        # Check for possible shuntsu with one additional tile
        for num in unique_numbers:
            if (num + 1 not in unique_numbers) and (num + 2 not in unique_numbers):
                if (num + 1 <= 9) or (num - 1 >= 1):
                    needed = min(needed, 1)  # Can form a shuntsu with one tile

    return needed

# Read input
tiles = input().strip()
# Output the result
print(min_tiles_to_draw(tiles))