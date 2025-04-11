def min_tiles_to_draw(tiles):
    hand = [(int(tile[0]), tile[1]) for tile in tiles]

    def has_koutsu(hand):
        counts = {}
        for number, suit in hand:
            counts[(number, suit)] = counts.get((number, suit), 0) + 1
        return any(count == 3 for count in counts.values())

    def has_shuntsu(hand):
        suits = {}
        for number, suit in hand:
            suits.setdefault(suit, []).append(number)

        for numbers in suits.values():
            numbers.sort()
            for i in range(len(numbers) - 2):
                if (numbers[i] + 1 in numbers) and (numbers[i] + 2 in numbers):
                    return True
        return False

    if has_koutsu(hand) or has_shuntsu(hand):
        return 0

    needed = float('inf')

    # Check for koutsu formation
    for number, suit in hand:
        needed = min(needed, 1)

    # Check for shuntsu formation
    suits = {}
    for number, suit in hand:
        suits.setdefault(suit, []).append(number)

    for numbers in suits.values():
        numbers.sort()
        for i in range(len(numbers)):
            if i > 0 and i < len(numbers) - 1:
                if numbers[i - 1] + 1 == numbers[i] and numbers[i] + 1 == numbers[i + 1]:
                    needed = min(needed, 0)
            if i == 0 and numbers[i] + 1 not in numbers:
                needed = min(needed, 1)
            if i == len(numbers) - 1 and numbers[i] - 1 not in numbers:
                needed = min(needed, 1)

    return needed

# Input reading
tiles = input().strip().split()
# Output the result
print(min_tiles_to_draw(tiles))