def solve():
    n = int(input())
    a1, a2, a3 = map(int, input().split())
    b1, b2, b3 = map(int, input().split())

    min_wins = 0
    
    rem_a1 = a1
    rem_a2 = a2
    rem_a3 = a3
    rem_b1 = b1
    rem_b2 = b2
    rem_b3 = b3

    min_wins = max(0, a1 - (b1 + b3 - n + a1), a2 - (b2 + b1 - n + a2), a3 - (b3 + b2 - n + a3))
    min_wins = max(0, a1 - (n - a1 - a2 + a2), a2 - (n - a2 - a3 + a3), a3 - (n - a3 - a1 + a1))
    min_wins = max(0, a1 - (b1 + b3 - (a1+a2+a3) + a1), a2 - (b2 + b1- (a1+a2+a3) + a2), a3 - (b3 + b2 - (a1+a2+a3) + a3))
    min_wins = max(0, a1 - (b1 + b3 - (a2+a3)), a2 - (b2 + b1- (a1+a3)), a3 - (b3 + b2 - (a1+a2)))

    max_wins = min(a1, b2) + min(a2, b3) + min(a3, b1)

    print(min_wins, max_wins)

solve()