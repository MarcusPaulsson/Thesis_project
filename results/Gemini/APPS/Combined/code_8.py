def solve():
    tiles = input().split()

    def is_mentsu(hand):
        # Check for koutsu
        for tile in set(hand):
            if hand.count(tile) >= 3:
                return True

        # Check for shuntsu
        suits = set(tile[1] for tile in hand)
        for suit in suits:
            nums = sorted([int(tile[0]) for tile in hand if tile[1] == suit])
            if len(nums) >= 3:
                for i in range(len(nums) - 2):
                    if nums[i+1] == nums[i] + 1 and nums[i+2] == nums[i] + 2:
                        return True
        return False

    if is_mentsu(tiles):
        print(0)
        return

    # Check for one tile draw
    for i in range(1, 10):
        for suit in ['m', 'p', 's']:
            new_tiles = tiles + [str(i) + suit]
            if is_mentsu(new_tiles):
                print(1)
                return

    print(2)

solve()