def solve():
    x = float(input())
    
    for a in range(1, 11):
        for b in range(1, 11):
            if abs((a * b)**0.5 - x) < 1e-6:
                print(a, b)
                return

solve()