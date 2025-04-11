def min_tiles_to_draw(tiles):
    # Parse the input tiles
    hand = [(int(tile[0]), tile[1]) for tile in tiles]
    
    # Count occurrences of each tile
    counts = {}
    for num, suit in hand:
        counts[(num, suit)] = counts.get((num, suit), 0) + 1
    
    # Check for koutsu (triplet)
    if any(count == 3 for count in counts.values()):
        return 0  # Already have a koutsu
    
    # Organize tiles by suit
    suits = {'m': [], 'p': [], 's': []}
    for num, suit in hand:
        suits[suit].append(num)
    
    # Check for shuntsu (sequence)
    for suit in suits:
        nums = sorted(suits[suit])
        if len(nums) >= 3:
            for i in range(len(nums) - 2):
                if nums[i] + 1 == nums[i + 1] and nums[i + 1] + 1 == nums[i + 2]:
                    return 0  # Already have a shuntsu
    
    # Calculate the minimum tiles needed to draw
    needed = float('inf')
    
    for suit in suits:
        nums = sorted(suits[suit])
        for i in range(len(nums)):
            # Check for potential shuntsu with one draw
            if nums[i] > 1 and (nums[i] - 1) not in nums:
                needed = min(needed, 1)  # Can draw (num[i] - 1)
            if nums[i] < 9 and (nums[i] + 1) not in nums:
                needed = min(needed, 1)  # Can draw (num[i] + 1)
            if i < len(nums) - 1 and nums[i + 1] - nums[i] > 1:
                needed = min(needed, 2)  # Need two draws to fill the gap
    
    return needed if needed != float('inf') else 2  # If no possible shuntsu, need at least 2 draws

# Read input
tiles = input().strip().split()
# Output the result
print(min_tiles_to_draw(tiles))