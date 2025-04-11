def min_tiles_to_draw(tiles):
    suits = {'m': [], 'p': [], 's': []}
    
    # Organize tiles by suit
    for tile in tiles:
        number = int(tile[0])
        suit = tile[1]
        suits[suit].append(number)
    
    # Check for koutsu (triplet)
    for suit in suits:
        if len(suits[suit]) == 3 and len(set(suits[suit])) == 1:
            return 0  # Already has a koutsu
    
    # Check for shuntsu (sequence)
    for suit in suits:
        numbers = sorted(suits[suit])
        if len(numbers) >= 3:
            for i in range(len(numbers) - 2):
                if numbers[i] + 1 == numbers[i + 1] and numbers[i] + 2 == numbers[i + 2]:
                    return 0  # Already has a shuntsu
    
    # Check for potential shuntsu with one draw
    for suit in suits:
        numbers = sorted(suits[suit])
        for number in numbers:
            if number - 1 >= 1 and number + 1 <= 9:
                if (number - 1 in numbers) or (number + 1 in numbers):
                    return 1  # Can form a shuntsu with one draw
    
    # If no mentsu can be formed with one draw, check for two draws
    for suit in suits:
        if len(suits[suit]) == 2:
            if abs(suits[suit][0] - suits[suit][1]) == 1:
                return 1  # Can form a shuntsu with one draw
            if (suits[suit][0] == 1 and suits[suit][1] == 2) or (suits[suit][0] == 8 and suits[suit][1] == 9):
                return 1  # Can form a shuntsu with one draw
            if (suits[suit][0] == 2 and suits[suit][1] == 3) or (suits[suit][0] == 7 and suits[suit][1] == 8):
                return 1  # Can form a shuntsu with one draw
    
    return 2  # Otherwise, need two draws

# Read input
tiles = input().strip().split()
# Output the result
print(min_tiles_to_draw(tiles))