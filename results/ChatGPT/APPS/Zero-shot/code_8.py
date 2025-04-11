def min_draws_to_win(tiles):
    from collections import defaultdict

    # Parse the input tiles
    hand = tiles.split()
    suits = defaultdict(list)

    for tile in hand:
        num = int(tile[0])
        suit = tile[1]
        suits[suit].append(num)

    # Check for koutsu (triplet)
    for suit in suits:
        if len(suits[suit]) == 3 and suits[suit].count(suits[suit][0]) == 3:
            return 0

    # Check for shuntsu (sequence)
    for suit in suits:
        nums = sorted(suits[suit])
        if len(nums) >= 3:
            for i in range(len(nums) - 2):
                if nums[i] + 1 == nums[i + 1] and nums[i] + 2 == nums[i + 2]:
                    return 0

    # Check for possible shuntsu with one draw
    for suit in suits:
        nums = sorted(suits[suit])
        if len(nums) == 2:
            # Check if we can form a sequence with one draw
            if (nums[0] + 1 == nums[1]) or (nums[0] + 2 == nums[1]) or (nums[1] - 1 == nums[0]) or (nums[1] - 2 == nums[0]):
                return 1
            if (nums[0] == 1 and nums[1] == 2) or (nums[0] == 2 and nums[1] == 3):
                return 1
        elif len(nums) == 1:
            # Check if we can form a sequence with one draw
            if nums[0] > 1 and nums[0] < 9:
                return 1
            elif nums[0] == 1 or nums[0] == 9:
                return 1

    # If we have no pairs or sequences, we need at least 2 draws
    return 2

# Read input
tiles = input().strip()
# Output the result
print(min_draws_to_win(tiles))