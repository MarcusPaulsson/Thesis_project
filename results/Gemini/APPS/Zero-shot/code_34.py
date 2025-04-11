def solve():
    n, a, b = map(int, input().split())
    
    max_x = 0
    for plates_a in range(1, n):
        plates_b = n - plates_a
        
        if plates_a > a or plates_b > b:
            continue
        
        x_a = a // plates_a
        x_b = b // plates_b
        
        max_x = max(max_x, min(x_a, x_b))
        
    print(max_x)

solve()