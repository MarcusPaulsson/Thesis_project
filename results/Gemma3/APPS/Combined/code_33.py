def solve():
    a1, b1, a2, b2, l, r = map(int, input().split())
    
    count = 0
    
    # Find the first x in the range [L, R] that satisfies x = a1*k + b1
    start_k = (l - b1 + a1 - 1) // a1  # Ceiling division
    
    x = a1 * start_k + b1
    
    while x <= r:
        # Check if x also satisfies x = a2*l + b2
        if (x - b2) % a2 == 0 and (x - b2) // a2 >= 0:
            count += 1
        
        start_k += 1
        x = a1 * start_k + b1
        
    print(count)

solve()