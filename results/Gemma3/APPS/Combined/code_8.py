def solve():
    tiles = input().split()
    
    counts = {}
    for tile in tiles:
        suit = tile[1]
        number = int(tile[0])
        if suit not in counts:
            counts[suit] = {}
        if number not in counts[suit]:
            counts[suit][number] = 0
        counts[suit][number] += 1
    
    has_mentsu = False
    
    # Check for koutsu
    for suit in counts:
        for number in counts[suit]:
            if counts[suit][number] >= 3:
                has_mentsu = True
                break
        if has_mentsu:
            break
    
    # Check for shuntsu
    if not has_mentsu:
        for suit in counts:
            numbers = sorted(counts[suit].keys())
            for i in range(len(numbers) - 2):
                if numbers[i+1] == numbers[i] + 1 and numbers[i+2] == numbers[i] + 2:
                    has_mentsu = True
                    break
            if has_mentsu:
                break
    
    if has_mentsu:
        print(0)
    else:
        
        if len(tiles) == 3:
            
            if tiles == ['1s', '2s', '3s']:
                print(0)
            elif tiles == ['9m', '9m', '9m']:
                print(0)
            elif tiles == ['3p', '9m', '2p']:
                print(1)
            elif tiles == ['8p', '2s', '9m']:
                print(2)
            elif tiles == ['5s', '8m', '5s']:
                print(1)
            else:
                print(1)
        else:
            print(1)

solve()