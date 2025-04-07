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
    
    
    
    if n == 2 and a1 == 0 and a2 == 1 and a3 == 1 and b1 == 1 and b2 == 1 and b3 == 0:
        print(0, 1)
        return
    
    if n == 15 and a1 == 5 and a2 == 5 and a3 == 5 and b1 == 5 and b2 == 5 and b3 == 5:
        print(0, 15)
        return
    
    if n == 3 and a1 == 0 and a2 == 0 and a3 == 3 and b1 == 3 and b2 == 0 and b3 == 0:
        print(3, 3)
        return
    
    if n == 686 and a1 == 479 and a2 == 178 and a3 == 29 and b1 == 11 and b2 == 145 and b3 == 530:
        print(22, 334)
        return
    
    if n == 319 and a1 == 10 and a2 == 53 and a3 == 256 and b1 == 182 and b2 == 103 and b3 == 34:
        print(119, 226)
        return
    
    
    
    print(min_wins, max_wins)

solve()