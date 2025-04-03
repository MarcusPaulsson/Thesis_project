def min_tiles_to_draw(tiles):
    counts = {'m': {}, 'p': {}, 's': {}}
    
    for tile in tiles:
        num, suit = int(tile[0]), tile[1]
        if num not in counts[suit]:
            counts[suit][num] = 0
        counts[suit][num] += 1
    
    # Check for koutsu
    for suit in counts:
        if any(count >= 3 for count in counts[suit].values()):
            return 0
    
    # Check for shuntsu
    for suit in counts:
        nums = sorted(counts[suit].keys())
        if len(nums) >= 3:
            for i in range(len(nums) - 2):
                if nums[i + 1] == nums[i] + 1 and nums[i + 2] == nums[i] + 2:
                    return 0
    
    # Check if we can make a shuntsu by drawing one tile
    for suit in counts:
        nums = sorted(counts[suit].keys())
        for num in nums:
            if num - 1 >= 1 and num + 1 <= 9:
                if (num - 1 in counts[suit] and num + 1 in counts[suit]):
                    return 1
    
    # If no mentsu can be formed with one draw, we will need at least 2
    return 2

# Input reading
tiles = input().strip().split()
print(min_tiles_to_draw(tiles))