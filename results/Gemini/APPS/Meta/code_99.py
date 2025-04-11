def solve():
    n = int(input())
    a1, a2, a3 = map(int, input().split())
    b1, b2, b3 = map(int, input().split())

    min_wins = max(0, a1 - (b1 + b3 - a3) , a2 - (b2 + b1 - a1) , a3 - (b3 + b2 - a2) , 0)
    min_wins = 0
    
    temp_a1, temp_a2, temp_a3 = a1, a2, a3
    temp_b1, temp_b2, temp_b3 = b1, b2, b3
    
    wins = 0
    
    wins += max(0, min(a1, b2))
    a1 -= min(a1, b2)
    b2 -= min(temp_a1, temp_b2)
    
    wins += max(0, min(a2, b3))
    a2 -= min(a2, b3)
    b3 -= min(temp_a2, temp_b3)
    
    wins += max(0, min(a3, b1))
    a3 -= min(a3, b1)
    b1 -= min(temp_a3, temp_b1)
    
    max_wins = wins
    
    print(min_wins, max_wins)

solve()