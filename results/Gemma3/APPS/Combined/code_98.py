def solve():
    n = int(input())
    
    if n == 2:
        print(1)
        return
    
    min_moves = float('inf')
    
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            j = n // i
            moves = (i - 1) + (j - 1)
            min_moves = min(min_moves, moves)
            
    print(min_moves)

solve()