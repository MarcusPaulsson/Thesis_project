def solve():
    a, b, c = map(int, input().split())
    
    best_cost = float('inf')
    best_triple = None
    
    for A in range(1, 2 * a + 1):
        for B in range(A, 2 * b + 1, A):
            C1 = (c // B) * B
            C2 = C1 + B
            
            candidates = []
            if C1 > 0:
                candidates.append(C1)
            candidates.append(C2)
            
            for C in candidates:
                cost = abs(a - A) + abs(b - B) + abs(c - C)
                if cost < best_cost:
                    best_cost = cost
                    best_triple = (A, B, C)
    
    print(best_cost)
    print(*best_triple)

t = int(input())
for _ in range(t):
    solve()