def solve():
    tiles = input().split()

    def check_mentsu(hand):
        counts = {}
        for tile in hand:
            counts[tile] = counts.get(tile, 0) + 1

        for tile in counts:
            if counts[tile] >= 3:
                return True

        nums = []
        suits = []
        for tile in hand:
            nums.append(int(tile[0]))
            suits.append(tile[1])

        if len(hand) < 3:
            return False
        
        for i in range(len(hand)):
            for j in range(i + 1, len(hand)):
                for k in range(j + 1, len(hand)):
                    if suits[i] == suits[j] == suits[k]:
                        a = nums[i]
                        b = nums[j]
                        c = nums[k]
                        
                        sorted_nums = sorted([a, b, c])
                        if sorted_nums[1] == sorted_nums[0] + 1 and sorted_nums[2] == sorted_nums[1] + 1:
                            return True
        return False

    if check_mentsu(tiles):
        print(0)
        return

    counts = {}
    for tile in tiles:
        counts[tile] = counts.get(tile, 0) + 1

    for tile in counts:
        if counts[tile] == 2:
            print(1)
            return
    
    nums = []
    suits = []
    for tile in tiles:
        nums.append(int(tile[0]))
        suits.append(tile[1])

    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            if suits[i] == suits[j]:
                a = nums[i]
                b = nums[j]
                if abs(a - b) <= 2:
                    print(1)
                    return

    print(2)

solve()