def min_draws(tiles):
    def is_koutsu(tiles):
        return len(set(tiles)) == 1

    def is_shuntsu(tiles):
        suits = {}
        for tile in tiles:
            num, suit = int(tile[0]), tile[1]
            if suit not in suits:
                suits[suit] = []
            suits[suit].append(num)
        
        for suit, numbers in suits.items():
            if len(numbers) >= 3:
                numbers.sort()
                for i in range(len(numbers) - 2):
                    if (numbers[i] + 1 in numbers and
                        numbers[i] + 2 in numbers):
                        return True
        return False

    if is_koutsu(tiles) or is_shuntsu(tiles):
        return 0

    # Check for possible shuntsu with one draw
    for tile in tiles:
        num, suit = int(tile[0]), tile[1]
        if (num - 1 >= 1 and num + 1 <= 9):
            if (str(num - 1) + suit not in tiles and
                str(num + 1) + suit not in tiles):
                return 1

    # Check for possible shuntsu with two draws
    for tile in tiles:
        num, suit = int(tile[0]), tile[1]
        if (num - 1 >= 1 and
            str(num - 1) + suit not in tiles):
            return 2
        if (num + 1 <= 9 and
            str(num + 1) + suit not in tiles):
            return 2

    return 2  # In the worst case, we need to draw 2 tiles

tiles = input().strip().split()
print(min_draws(tiles))