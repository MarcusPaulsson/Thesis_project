def solve():
    a, b = map(int, input().split())
    total = a + b
    
    min_perimeter = float('inf')
    
    for h in range(1, int(total**0.5) + 2):
        if total % h == 0:
            w = total // h
            
            # Case 1: a forms a rectangle
            for h_a in range(1, int(a**0.5) + 2):
                if a % h_a == 0:
                    w_a = a // h_a
                    if h_a <= h and w_a <= w:
                        min_perimeter = min(min_perimeter, 2 * (h + w))
            
            # Case 2: b forms a rectangle
            for h_b in range(1, int(b**0.5) + 2):
                if b % h_b == 0:
                    w_b = b // h_b
                    if h_b <= h and w_b <= w:
                        min_perimeter = min(min_perimeter, 2 * (h + w))
    
    print(min_perimeter)

solve()