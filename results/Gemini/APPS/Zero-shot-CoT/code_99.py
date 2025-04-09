def solve():
    n = int(input())
    a1, a2, a3 = map(int, input().split())
    b1, b2, b3 = map(int, input().split())

    min_wins = max(0, a1 - (b1 + b3) + max(0, b1 - a2 - a3) + max(0, b3 - a1 - a2),
                   a2 - (b2 + b1) + max(0, b2 - a1 - a3) + max(0, b1 - a2 - a3),
                   a3 - (b3 + b2) + max(0, b3 - a1 - a2) + max(0, b2 - a1 - a3))

    max_wins = min(a1, b2) + min(a2, b3) + min(a3, b1)

    print(min_wins, max_wins)

solve()