def min_draws_to_win(tiles):
    from collections import Counter

    def has_koutsu(tiles):
        counts = Counter(tiles)
        return any(count == 3 for count in counts.values())

    def has_shuntsu(tiles):
        suits = {'m': [], 'p': [], 's': []}
        for tile in tiles:
            num = int(tile[0])
            suit = tile[1]
            suits[suit].append(num)

        for suit_tiles in suits.values():
            suit_tiles.sort()
            for i in range(len(suit_tiles) - 2):
                if (suit_tiles[i + 1] == suit_tiles[i] + 1 and 
                    suit_tiles[i + 2] == suit_tiles[i] + 2):
                    return True
        return False

    if has_koutsu(tiles) or has_shuntsu(tiles):
        return 0

    counts = Counter(tiles)
    for tile in tiles:
        num, suit = int(tile[0]), tile[1]
        
        if counts[tile] < 3:
            return 1  # Need one more for koutsu

        if (num > 1 and (num - 1) in counts and (num + 1) in counts):
            return 0  # Already can form shuntsu

        if num == 1:
            return 2 if (2 not in counts) else 1
        elif num == 9:
            return 2 if (8 not in counts) else 1
        else:
            if (num - 1 in counts and num + 1 in counts):
                return 0
            elif (num - 1 in counts or num + 1 in counts):
                return 1
            else:
                return 2

    return 2  # If nothing is possible

tiles = input().strip().split()
print(min_draws_to_win(tiles))