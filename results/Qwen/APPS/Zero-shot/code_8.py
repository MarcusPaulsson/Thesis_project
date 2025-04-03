def min_extra_tiles(tiles):
    suits = {'m': 0, 'p': 0, 's': 0}
    numbers = [0] * 9
    for tile in tiles:
        suits[tile[1]] += 1
        numbers[int(tile[0]) - 1] += 1
    extra_tiles = 0
    for i in range(9):
        if numbers[i] < 3:
            extra_tiles += 3 - numbers[i]
    return extra_tiles

tiles = input().split()
print(min_extra_tiles(tiles))