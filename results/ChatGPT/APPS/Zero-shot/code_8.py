def can_form_koutsu(tiles):
    from collections import Counter
    count = Counter(tiles)
    return any(v >= 3 for v in count.values())

def can_form_shuntsu(tiles):
    suits = {'m': [], 'p': [], 's': []}
    for tile in tiles:
        number = int(tile[0])
        suit = tile[1]
        suits[suit].append(number)

    for numbers in suits.values():
        numbers.sort()
        for i in range(len(numbers) - 2):
            if (numbers[i] + 1 in numbers) and (numbers[i] + 2 in numbers):
                return True
    return False

def min_draws(tiles):
    if can_form_koutsu(tiles) or can_form_shuntsu(tiles):
        return 0

    # Check for koutsu possibility by adding a tile
    for tile in tiles:
        if tiles.count(tile) < 2:
            return 1  # Drawing a third tile for a koutsu

    # Check for shuntsu possibility by adding a tile
    suits = {'m': [], 'p': [], 's': []}
    for tile in tiles:
        number = int(tile[0])
        suit = tile[1]
        suits[suit].append(number)

    for suit in suits:
        numbers = sorted(suits[suit])
        for number in numbers:
            if number - 1 not in numbers and number + 1 not in numbers:
                return 1  # Drawing a tile to complete a shuntsu

    return 2  # At worst, we need to draw 2 tiles

tiles = input().split()
print(min_draws(tiles))