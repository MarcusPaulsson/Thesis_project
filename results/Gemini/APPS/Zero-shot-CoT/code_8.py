def solve():
    tiles = input().split()
    
    def check_mentsu(arr):
        if len(arr) < 3:
            return False
        
        # Check for koutsu
        for i in range(len(arr) - 2):
            if arr[i] == arr[i+1] and arr[i] == arr[i+2]:
                return True
        
        # Check for shuntsu
        nums = []
        suits = []
        for tile in arr:
            nums.append(int(tile[0]))
            suits.append(tile[1])
        
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                for k in range(j + 1, len(arr)):
                    if suits[i] == suits[j] and suits[i] == suits[k]:
                        vals = sorted([nums[i], nums[j], nums[k]])
                        if vals[1] == vals[0] + 1 and vals[2] == vals[1] + 1:
                            return True
        
        return False

    if check_mentsu(tiles):
        print(0)
        return

    nums = []
    suits = []
    for tile in tiles:
        nums.append(int(tile[0]))
        suits.append(tile[1])
    
    # Check if adding one tile can form a mentsu
    for num in range(1, 10):
        for suit in ['m', 'p', 's']:
            new_tile = str(num) + suit
            new_tiles = tiles + [new_tile]
            if check_mentsu(new_tiles):
                print(1)
                return

    # Check if adding two tiles can form a mentsu
    for num1 in range(1, 10):
        for suit1 in ['m', 'p', 's']:
            new_tile1 = str(num1) + suit1
            for num2 in range(1, 10):
                for suit2 in ['m', 'p', 's']:
                    new_tile2 = str(num2) + suit2
                    new_tiles = tiles + [new_tile1, new_tile2]
                    if check_mentsu(new_tiles):
                        print(2)
                        return
    
    print(2)

solve()