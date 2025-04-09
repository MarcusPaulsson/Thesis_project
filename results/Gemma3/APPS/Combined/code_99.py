def solve():
    n = int(input())
    a1, a2, a3 = map(int, input().split())
    b1, b2, b3 = map(int, input().split())
    
    min_wins = 0
    max_wins = 0
    
    # Calculate minimum wins
    min_wins = min(a1, b2) + min(a2, b3) + min(a3, b1)
    
    # Calculate maximum wins
    max_wins = min(a1, b3) + min(a2, b1) + min(a3, b2)
    
    print(min_wins, max_wins)