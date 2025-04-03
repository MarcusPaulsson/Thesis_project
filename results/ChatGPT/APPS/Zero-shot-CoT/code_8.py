def min_tiles_to_draw(tiles):
    from collections import defaultdict

    suits = defaultdict(list)
    
    # Parse the input tiles
    for tile in tiles:
        number = int(tile[0])
        suit = tile[1]
        suits[suit].append(number)

    # Check for koutsu (triplet)
    for suit in suits:
        if len(suits[suit]) == 3 and len(set(suits[suit])) == 1:
            return 0  # Already has a koutsu

    # Check for shuntsu (sequence)
    for suit in suits:
        if len(suits[suit]) >= 3:
            sorted_numbers = sorted(set(suits[suit]))
            for i in range(len(sorted_numbers) - 2):
                if sorted_numbers[i + 1] == sorted_numbers[i] + 1 and sorted_numbers[i + 2] == sorted_numbers[i] + 2:
                    return 0  # Already has a shuntsu

    # Try to form a shuntsu by drawing one tile
    for suit in suits:
        existing_numbers = set(suits[suit])
        for number in range(1, 10):
            if (number + 1 in existing_numbers and number + 2 in existing_numbers) or \
               (number - 1 in existing_numbers and number + 1 in existing_numbers) or \
               (number - 2 in existing_numbers and number - 1 in existing_numbers):
                return 1  # Can form a shuntsu by drawing one tile

    # If no mentsu can be formed, it requires at least 2 draws
    return 2

# Read input
tiles = input().strip().split()
# Output the result
print(min_tiles_to_draw(tiles))