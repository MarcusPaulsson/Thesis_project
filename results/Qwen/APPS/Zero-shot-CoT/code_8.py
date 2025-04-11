def min_extra_tiles(tiles):
    suits = {'m': 0, 'p': 0, 's': 0}
    numbers = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    
    for tile in tiles:
        suit = tile[1]
        number = int(tile[0])
        suits[suit] += 1
        numbers[number] += 1
    
    extra_tiles = 0
    
    for suit in suits.values():
        if suit < 3:
            extra_tiles += (3 - suit)
    
    for number in numbers.values():
        if number < 3:
            extra_tiles += (3 - number)
    
    return extra_tiles

# Read input
tiles = input().split()

# Calculate and print the minimum number of extra tiles needed
print(min_extra_tiles(tiles))