def solve():
    n = int(input())
    a1, a2, a3 = map(int, input().split())
    b1, b2, b3 = map(int, input().split())

    max_wins = 0
    max_wins += min(a1, b2)
    max_wins += min(a2, b3)
    max_wins += min(a3, b1)

    min_wins = max(0, a1 - (b1 + b3), a2 - (b2 + b1), a3 - (b3 + b2))
    
    print(min_wins, max_wins)

solve()