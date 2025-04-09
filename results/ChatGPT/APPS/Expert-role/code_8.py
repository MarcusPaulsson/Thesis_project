def min_extra_tiles(tiles):
    tile_counts = {}
    for tile in tiles:
        num, suit = int(tile[0]), tile[1]
        if suit not in tile_counts:
            tile_counts[suit] = {}
        if num not in tile_counts[suit]:
            tile_counts[suit][num] = 0
        tile_counts[suit][num] += 1

    # Check for koutsu (triplet)
    for suit in tile_counts:
        for num in tile_counts[suit]:
            if tile_counts[suit][num] >= 3:
                return 0

    # Check for shuntsu (sequence)
    for suit in tile_counts:
        nums = sorted(tile_counts[suit].keys())
        for i in range(len(nums) - 2):
            if nums[i] + 1 == nums[i + 1] and nums[i + 1] + 1 == nums[i + 2]:
                return 0

        # Check what we need to form a shuntsu
        for num in nums:
            if num - 1 in tile_counts[suit] and num + 1 in tile_counts[suit]:
                return 0

    # Check how many tiles we need to draw
    needed = 2  # At most we can need 2 tiles to form a shuntsu
    for suit in tile_counts:
        nums = sorted(tile_counts[suit].keys())
        for num in nums:
            if num - 1 not in tile_counts[suit] and num + 1 not in tile_counts[suit]:
                needed = min(needed, 2)  # Need 2 specific tiles
            else:
                needed = min(needed, 1)  # Need only 1 tile

    return needed

# Input handling
tiles = input().strip().split()
print(min_extra_tiles(tiles))