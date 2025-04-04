def can_form_koutsu(tiles):
    tile_count = {}
    for tile in tiles:
        tile_count[tile] = tile_count.get(tile, 0) + 1
    return any(count >= 3 for count in tile_count.values())

def can_form_shuntsu(tiles):
    suit_dict = {'m': [], 'p': [], 's': []}
    for tile in tiles:
        num = int(tile[0])
        suit = tile[1]
        suit_dict[suit].append(num)
    
    for nums in suit_dict.values():
        nums = sorted(set(nums))  # Use set to avoid duplicates
        if len(nums) >= 3:
            for i in range(len(nums) - 2):
                if nums[i] + 1 in nums and nums[i] + 2 in nums:
                    return True
    return False

tiles = input().strip().split()

if can_form_koutsu(tiles) or can_form_shuntsu(tiles):
    print(0)
else:
    possible_draws = set()
    for tile in tiles:
        num = int(tile[0])
        suit = tile[1]
        if num > 1:  # Prevent negative numbers
            possible_draws.add(f"{num-1}{suit}")
        if num < 9:  # Prevent numbers greater than 9
            possible_draws.add(f"{num+1}{suit}")
    
    for draw in possible_draws:
        if can_form_koutsu(tiles + [draw]) or can_form_shuntsu(tiles + [draw]):
            print(1)
            break
    else:
        print(2)