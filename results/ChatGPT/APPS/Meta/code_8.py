def min_extra_tiles(tiles):
    # Split the input into a list of tiles
    tiles = tiles.split()
    
    # Count the occurrences of each tile
    counts = {}
    for tile in tiles:
        counts[tile] = counts.get(tile, 0) + 1
    
    # Check for koutsu (triplet)
    if any(count == 3 for count in counts.values()):
        return 0
    
    # Check for shuntsu (sequence) possibilities
    suits = {'m': [], 'p': [], 's': []}
    for tile in tiles:
        num, suit = int(tile[0]), tile[1]
        suits[suit].append(num)
    
    # Sort the numbers for each suit
    for suit in suits:
        suits[suit].sort()
    
    # Check for shuntsu in each suit
    for suit, numbers in suits.items():
        if len(numbers) >= 3:
            for i in range(len(numbers) - 2):
                if numbers[i] + 1 == numbers[i + 1] and numbers[i] + 2 == numbers[i + 2]:
                    return 0
    
    # Check for shuntsu possibilities with one draw
    for suit, numbers in suits.items():
        for num in numbers:
            if num - 1 >= 1 and num + 1 <= 9:
                if (num - 1 not in numbers) or (num + 1 not in numbers):
                    return 1
    
    # If no shuntsu or koutsu can be formed, it requires two draws
    return 2

# Read input
tiles = input().strip()
# Get the result
result = min_extra_tiles(tiles)
# Print the result
print(result)