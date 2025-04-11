def solve():
    n = int(input())
    a1, a2, a3 = map(int, input().split())
    b1, b2, b3 = map(int, input().split())

    # Calculate maximum wins
    max_wins = min(a1, b2) + min(a2, b3) + min(a3, b1)

    # Calculate minimum wins
    min_wins = 0
    
    rem_a1, rem_a2, rem_a3 = a1, a2, a3
    rem_b1, rem_b2, rem_b3 = b1, b2, b3

    
    lose_a1 = min(rem_a1, rem_b1)
    rem_a1 -= lose_a1
    rem_b1 -= lose_a1

    lose_a1 = min(rem_a1, rem_b3)
    rem_a1 -= lose_a1
    rem_b3 -= lose_a1
    
    lose_a2 = min(rem_a2, rem_b2)
    rem_a2 -= lose_a2
    rem_b2 -= lose_a2

    lose_a2 = min(rem_a2, rem_b1)
    rem_a2 -= lose_a2
    rem_b1 -= lose_a2

    lose_a3 = min(rem_a3, rem_b3)
    rem_a3 -= lose_a3
    rem_b3 -= lose_a3

    lose_a3 = min(rem_a3, rem_b2)
    rem_a3 -= lose_a3
    rem_b2 -= lose_a3

    min_wins = max(0, n - (min(a1, b1) + min(a1, b3) + min(a2, b2) + min(a2, b1) + min(a3, b3) + min(a3, b2)))
    
    print(min_wins, max_wins)

solve()