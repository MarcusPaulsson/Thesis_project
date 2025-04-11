def solve():
    tiles = input().split()
    
    def check_mentsu(hand):
        # Check for koutsu
        counts = {}
        for tile in hand:
            counts[tile] = counts.get(tile, 0) + 1
        for tile, count in counts.items():
            if count >= 3:
                return True
        
        # Check for shuntsu
        suits = ['m', 'p', 's']
        for suit in suits:
            nums = []
            for tile in hand:
                if tile[1] == suit:
                    nums.append(int(tile[0]))
            nums.sort()
            
            if len(nums) >= 3:
                for i in range(len(nums) - 2):
                    if nums[i+1] == nums[i] + 1 and nums[i+2] == nums[i] + 2:
                        return True
        
        return False

    if check_mentsu(tiles):
        print(0)
        return
    
    # Try drawing one tile
    for i in range(1, 10):
        for suit in ['m', 'p', 's']:
            new_tile = str(i) + suit
            new_hand = tiles + [new_tile]
            if check_mentsu(new_hand):
                print(1)
                return
    
    # Try drawing two tiles
    print(2)

solve()