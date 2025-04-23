def solve():
    n = int(input())
    a1, a2, a3 = map(int, input().split())
    b1, b2, b3 = map(int, input().split())

    min_wins = 0
    
    temp_a1 = a1
    temp_a2 = a2
    temp_a3 = a3
    temp_b1 = b1
    temp_b2 = b2
    temp_b3 = b3

    min_wins = max(0, a1 - (b1 + b3)) + max(0, a2 - (b2 + b1)) + max(0, a3 - (b3 + b2))
    
    max_wins = min(a1, b2) + min(a2, b3) + min(a3, b1)

    print(min_wins, max_wins)

solve()