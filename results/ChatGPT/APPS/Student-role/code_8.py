def min_tiles_to_draw(tiles):
    from collections import defaultdict

    # Parse the input tiles
    hand = [tile for tile in tiles.split()]
    
    # Check for koutsu (triplet)
    counts = defaultdict(int)
    for tile in hand:
        counts[tile] += 1
    
    # Check for koutsu
    if any(count == 3 for count in counts.values()):
        return 0
    
    # Check for shuntsu (sequence)
    suits = defaultdict(list)
    for tile in hand:
        num = int(tile[0])
        suit = tile[1]
        suits[suit].append(num)
    
    # Check for existing shuntsu
    for suit, numbers in suits.items():
        numbers.sort()
        for i in range(len(numbers) - 2):
            if numbers[i] + 1 == numbers[i + 1] and numbers[i] + 2 == numbers[i + 2]:
                return 0
    
    # If no mentsu, check how many tiles needed
    needed = 2  # Start with the maximum needed
    for suit, numbers in suits.items():
        numbers.sort()
        for i in range(len(numbers)):
            # Check for possible shuntsu with one draw
            if i > 0 and numbers[i] - 1 == numbers[i - 1]:
                needed = min(needed, 1)  # Can complete with one draw
            if i < len(numbers) - 1 and numbers[i] + 1 == numbers[i + 1]:
                needed = min(needed, 1)  # Can complete with one draw
            if i < len(numbers) - 1 and numbers[i] + 2 == numbers[i + 1]:
                needed = min(needed, 1)  # Can complete with one draw
            if i == 0 or (i > 0 and numbers[i] - 1 > numbers[i - 1] + 1):
                needed = min(needed, 2)  # Need two draws to complete a new sequence
    
    return needed

# Read input and output result
tiles = input().strip()
print(min_tiles_to_draw(tiles))