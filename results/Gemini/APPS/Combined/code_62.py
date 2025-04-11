def solve():
    a, b, c = map(int, input().split())
    
    best_cost = float('inf')
    best_abc = None
    
    for A in range(1, 2 * a + 1):
        for B in range(A, 2 * b + 1, A):
            for C in range(B, 2 * c + 1, B):
                cost = abs(a - A) + abs(b - B) + abs(c - C)
                if cost < best_cost:
                    best_cost = cost
                    best_abc = (A, B, C)
    
    print(best_cost)
    print(*best_abc)

t = int(input())
for _ in range(t):
    solve()