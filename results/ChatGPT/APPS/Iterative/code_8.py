def min_draws_to_win(tiles):
    from collections import defaultdict

    # Parse the input tiles
    hand = tiles.split()
    counts = defaultdict(int)
    suits = defaultdict(list)

    for tile in hand:
        number = int(tile[0])
        suit = tile[1]
        counts[(number, suit)] += 1
        suits[suit].append(number)

    # Check for existing mentsus
    def has_koutsu():
        return any(count >= 3 for count in counts.values())

    def has_shuntsu():
        for suit, numbers in suits.items():
            numbers = sorted(set(numbers))  # Unique and sorted numbers
            for i in range(len(numbers) - 2):
                if (numbers[i] + 1 in numbers) and (numbers[i] + 2 in numbers):
                    return True
        return False

    if has_koutsu() or has_shuntsu():
        return 0

    # Check for draws needed
    def can_form_shuntsu_with_one_draw():
        for suit, numbers in suits.items():
            numbers = sorted(set(numbers))  # Unique and sorted numbers
            for i in range(len(numbers)):
                if i > 0 and numbers[i] - 1 == numbers[i - 1]:  # Check for a pair
                    if numbers[i] + 1 not in numbers:  # Need the next number
                        return True
                if i < len(numbers) - 1 and numbers[i] + 1 == numbers[i + 1]:  # Check for a pair
                    if numbers[i] - 1 not in numbers:  # Need the previous number
                        return True
        return False

    if can_form_shuntsu_with_one_draw():
        return 1

    # If no mentsus and can't form with one draw, check for two draws
    return 2

# Read input
tiles = input().strip()
# Output the result
print(min_draws_to_win(tiles))