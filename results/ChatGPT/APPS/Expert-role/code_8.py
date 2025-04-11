def min_tiles_to_draw(tiles):
    from collections import defaultdict

    counts = defaultdict(int)
    for tile in tiles:
        counts[tile] += 1

    # Check for koutsu (triplet)
    for count in counts.values():
        if count == 3:
            return 0

    # Check for shuntsu (sequence)
    suits = defaultdict(list)
    for tile in tiles:
        num = int(tile[0])
        suit = tile[1]
        suits[suit].append(num)

    for suit in suits.values():
        suit.sort()
        for i in range(len(suit) - 2):
            if suit[i] + 1 == suit[i + 1] and suit[i] + 2 == suit[i + 2]:
                return 0

    # Check how many tiles are needed to form a shuntsu
    needed = float('inf')
    for suit in suits:
        nums = sorted(suits[suit])
        for i in range(len(nums)):
            # Check for possible sequences
            for j in range(3):
                target = nums[i] + j
                if target not in nums:
                    # Count how many tiles we need to draw
                    draw_count = 0
                    if target - 1 not in nums:
                        draw_count += 1
                    if target not in nums:
                        draw_count += 1
                    if target + 1 not in nums:
                        draw_count += 1
                    needed = min(needed, draw_count)

    return needed if needed != float('inf') else 2

tiles = input().split()
print(min_tiles_to_draw(tiles))