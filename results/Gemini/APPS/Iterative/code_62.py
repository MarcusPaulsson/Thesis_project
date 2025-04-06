def solve():
    a, b, c = map(int, input().split())
    
    best_cost = float('inf')
    best_triple = None
    
    for A in range(1, 2 * a + 1):
        for B in range(A, 2 * b + 1, A):
            C_candidates = []
            C_candidates.append(B * (c // B))
            C_candidates.append(B * (c // B + 1))
            
            for C in C_candidates:
                if C > 0:
                    cost = abs(a - A) + abs(b - B) + abs(c - C)
                    if cost < best_cost:
                        if A <= B <= C:
                            best_cost = cost
                            best_triple = (A, B, C)
    
    print(best_cost)
    print(*best_triple)

t = int(input())
for _ in range(t):
    solve()