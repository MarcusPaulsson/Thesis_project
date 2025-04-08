def min_tiles_to_draw(tiles):
    # Parse tiles into a structured format
    counts = {}
    for tile in tiles:
        num = int(tile[0])
        suit = tile[1]
        if suit not in counts:
            counts[suit] = []
        counts[suit].append(num)

    def has_koutsu(nums):
        return len(nums) == 3 and nums[0] == nums[1] == nums[2]

    def has_shuntsu(nums):
        if len(nums) < 3:
            return False
        nums.sort()
        for i in range(len(nums) - 2):
            if nums[i] + 1 == nums[i + 1] and nums[i + 1] + 1 == nums[i + 2]:
                return True
        return False

    # Check for existing mentsus
    for nums in counts.values():
        if has_koutsu(sorted(nums)) or has_shuntsu(sorted(nums)):
            return 0  # A mentsu already exists

    # Analyze potential draws for shuntsu
    for nums in counts.values():
        nums.sort()
        if len(nums) == 2:
            if abs(nums[0] - nums[1]) <= 2:
                return 1  # One draw can complete a shuntsu
            return 2  # Two draws needed to form a shuntsu
        elif len(nums) == 1:
            if nums[0] == 1 or nums[0] == 9:
                return 2  # Need two draws to form a shuntsu
            return 1  # One draw can complete a shuntsu

    # If no mentsu is found, need at least 2 tiles to draw
    return 2

# Read input
tiles = input().strip().split()
print(min_tiles_to_draw(tiles))