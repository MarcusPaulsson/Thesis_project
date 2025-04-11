def solve():
    tiles = input().split()
    
    def check_mentsu(hand):
        # Check for koutsu
        for i in range(len(hand)):
            count = 0
            for j in range(len(hand)):
                if hand[i] == hand[j]:
                    count += 1
            if count >= 3:
                return True
        
        # Check for shuntsu
        for i in range(len(hand)):
            for j in range(i + 1, len(hand)):
                for k in range(j + 1, len(hand)):
                    t1 = hand[i]
                    t2 = hand[j]
                    t3 = hand[k]
                    
                    if t1[1] == t2[1] == t3[1]:
                        nums = sorted([int(t1[0]), int(t2[0]), int(t3[0])])
                        if nums[1] == nums[0] + 1 and nums[2] == nums[1] + 1:
                            return True
        
        return False
    
    if check_mentsu(tiles):
        print(0)
        return
    
    # Try drawing one tile
    suits = ['m', 'p', 's']
    for i in range(1, 10):
        for suit in suits:
            new_tile = str(i) + suit
            new_hand = tiles + [new_tile]
            if check_mentsu(new_hand):
                print(1)
                return
    
    # Try drawing two tiles
    print(2)

solve()