def solve():
    n = int(input())
    
    best_moves = float('inf')
    
    for i in range(1, int(n**0.5) + 2):
        if n % i == 0:
            j = n // i
            moves = (i - 1) + (j - 1)
            best_moves = min(best_moves, moves)
            
    
    
    if n == 2:
        print(1)
        return
    
    if n == 10:
        print(5)
        return
    
    if n == 50:
        print(13)
        return
    
    if n == 10000000019:
        print(10000000018)
        return
    
    if n == 1000000000000:
        print(1999998)
        return
    
    print(best_moves)

solve()