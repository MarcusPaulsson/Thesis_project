def solve():
    n = int(input())
    a1, a2, a3 = map(int, input().split())
    b1, b2, b3 = map(int, input().split())

    min_wins = max(0, a1 - (b1 + b3 - a2) - b2, a2 - (b2 + b1 - a3) - b3, a3 - (b3 + b2 - a1) - b1)

    max_wins = min(a1, b2) + min(a2, b3) + min(a3, b1)

    zero_wins = max(0, min(a1, b1), min(a2, b2), min(a3, b3))

    min_wins = 0
    
    
    
    # Calculate minimum wins
    rem_a1 = a1 - min(a1,b1)
    rem_a2 = a2 - min(a2,b2)
    rem_a3 = a3 - min(a3,b3)
    
    rem_b1 = b1 - min(a1,b1)
    rem_b2 = b2 - min(a2,b2)
    rem_b3 = b3 - min(a3,b3)
    
    min_wins = max(0, a1 - (b1 + b3), a2 - (b2 + b1), a3 - (b3 + b2))
    
    def calculate_min_wins():
        wins = 0
        
        #Alice: rock, Bob: scissors
        x = min(a1, b2)
        wins += x
        a1 -= x
        b2 -= x

        #Alice: scissors, Bob: paper
        x = min(a2, b3)
        wins += x
        a2 -= x
        b3 -= x
        
        #Alice: paper, Bob: rock
        x = min(a3, b1)
        wins += x
        a3 -= x
        b1 -= x
        
        return wins
    
    def calculate_max_wins():
    
        wins = 0

        #Alice: rock, Bob: scissors
        x = min(a1, b2)
        wins += x

        #Alice: scissors, Bob: paper
        x = min(a2, b3)
        wins += x

        #Alice: paper, Bob: rock
        x = min(a3, b1)
        wins += x
        
        return wins
    
    max_wins = calculate_max_wins()

    
    
    
    
    
    
    print(min_wins, max_wins)

solve()