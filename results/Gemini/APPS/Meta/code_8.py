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
        suits = {'m': [], 'p': [], 's': []}
        for tile in hand:
            suits[tile[1]].append(int(tile[0]))
        
        for suit in suits.values():
            suit.sort()
            if len(suit) >= 3:
                for i in range(len(suit) - 2):
                    if suit[i+1] == suit[i] + 1 and suit[i+2] == suit[i] + 2:
                        return True
        
        return False

    if check_mentsu(tiles):
        print(0)
        return
    
    # Try adding one tile
    for i in range(1, 10):
        for suit in ['m', 'p', 's']:
            new_tile = str(i) + suit
            if check_mentsu(tiles + [new_tile]):
                print(1)
                return
    
    print(2)

solve()