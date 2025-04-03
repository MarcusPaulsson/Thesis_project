def min_extra_tiles(tiles):
    # Parse the input tiles into number and suit
    hand = [(int(tile[0]), tile[1]) for tile in tiles.split()]
    
    # Check for koutsu (triplet)
    def has_koutsu(hand):
        counts = {}
        for number, suit in hand:
            if (number, suit) in counts:
                counts[(number, suit)] += 1
            else:
                counts[(number, suit)] = 1
        return any(count == 3 for count in counts.values())

    # Check for shuntsu (sequence)
    def has_shuntsu(hand):
        suits = {}
        for number, suit in hand:
            if suit not in suits:
                suits[suit] = []
            suits[suit].append(number)

        for suit in suits:
            numbers = sorted(suits[suit])
            for i in range(len(numbers) - 2):
                if numbers[i] + 1 in numbers and numbers[i] + 2 in numbers:
                    return True
        return False
    
    # Check if already has a mentsu
    if has_koutsu(hand) or has_shuntsu(hand):
        print(0)
        return

    # Check if we can create mentsus by drawing one tile
    for number, suit in hand:
        # Check for shuntsu possibilities
        if suit == 'm':
            if number > 1 and number < 9:
                if (number - 1, 'm') in hand and (number + 1, 'm') not in hand:
                    print(1)
                    return
            elif number == 1:
                if (number + 1, 'm') in hand:
                    print(1)
                    return
            elif number == 9:
                if (number - 1, 'm') in hand:
                    print(1)
                    return
        elif suit == 'p':
            if number > 1 and number < 9:
                if (number - 1, 'p') in hand and (number + 1, 'p') not in hand:
                    print(1)
                    return
            elif number == 1:
                if (number + 1, 'p') in hand:
                    print(1)
                    return
            elif number == 9:
                if (number - 1, 'p') in hand:
                    print(1)
                    return
        elif suit == 's':
            if number > 1 and number < 9:
                if (number - 1, 's') in hand and (number + 1, 's') not in hand:
                    print(1)
                    return
            elif number == 1:
                if (number + 1, 's') in hand:
                    print(1)
                    return
            elif number == 9:
                if (number - 1, 's') in hand:
                    print(1)
                    return

    # If we reach here, we need to draw two tiles
    print(2)

# Input
tiles = input().strip()
min_extra_tiles(tiles)