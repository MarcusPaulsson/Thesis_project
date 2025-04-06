def solve():
    tiles = input().split()

    def check_mentsu(hand):
        counts = {}
        for tile in hand:
            if tile not in counts:
                counts[tile] = 0
            counts[tile] += 1

        for tile in counts:
            if counts[tile] >= 3:
                return True

        suits = {'m': [], 'p': [], 's': []}
        for tile in hand:
            suits[tile[1]].append(int(tile[0]))

        for suit in suits:
            suits[suit].sort()
            if len(suits[suit]) >= 3:
                for i in range(len(suits[suit]) - 2):
                    if suits[suit][i+1] == suits[suit][i] + 1 and suits[suit][i+2] == suits[suit][i] + 2:
                        return True

        return False

    if check_mentsu(tiles):
        print(0)
        return

    counts = {}
    for tile in tiles:
        if tile not in counts:
            counts[tile] = 0
        counts[tile] += 1

    for tile in counts:
        if counts[tile] >= 2:
            print(1)
            return
    
    suits = {'m': [], 'p': [], 's': []}
    for tile in tiles:
        suits[tile[1]].append(int(tile[0]))

    for suit in suits:
        suits[suit].sort()
        if len(suits[suit]) >= 2:
            for i in range(len(suits[suit])):
                for j in range(i + 1, len(suits[suit])):
                    if suits[suit][j] == suits[suit][i] + 1 or suits[suit][j] == suits[suit][i] + 2:
                        print(1)
                        return

    print(2)

solve()