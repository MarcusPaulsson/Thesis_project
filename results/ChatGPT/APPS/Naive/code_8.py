def min_tiles_to_draw(tiles):
    suits = {'m': [], 'p': [], 's': []}
    
    # Parse the tiles into suits
    for tile in tiles:
        number = int(tile[0])
        suit = tile[1]
        suits[suit].append(number)
    
    # Check for existing mentsus
    def has_koutsu(suit_tiles):
        return len(suit_tiles) >= 3 and len(set(suit_tiles)) == 1
    
    def has_shuntsu(suit_tiles):
        if len(suit_tiles) < 3:
            return False
        suit_tiles = sorted(set(suit_tiles))
        for i in range(len(suit_tiles) - 2):
            if suit_tiles[i] + 1 == suit_tiles[i + 1] and suit_tiles[i + 1] + 1 == suit_tiles[i + 2]:
                return True
        return False
    
    # Check if there's already a mentsu
    for suit in suits:
        if has_koutsu(suits[suit]) or has_shuntsu(suits[suit]):
            return 0
    
    # If no mentsu, calculate the minimum tiles needed
    needed = float('inf')
    
    # Check for koutsu possibilities
    for suit in suits:
        if len(suits[suit]) == 2:
            needed = min(needed, 1)  # Need one more tile to form a koutsu
        elif len(suits[suit]) == 1:
            needed = min(needed, 2)  # Need two more tiles to form a koutsu
    
    # Check for shuntsu possibilities
    for suit in suits:
        if len(suits[suit]) == 2:
            if abs(suits[suit][0] - suits[suit][1]) == 1:
                needed = min(needed, 1)  # Need one more tile to form a shuntsu
            else:
                needed = min(needed, 2)  # Need two more tiles to form a shuntsu
        elif len(suits[suit]) == 1:
            needed = min(needed, 2)  # Need two more tiles to form a shuntsu
    
    return needed

# Input reading
tiles = input().strip().split()
print(min_tiles_to_draw(tiles))