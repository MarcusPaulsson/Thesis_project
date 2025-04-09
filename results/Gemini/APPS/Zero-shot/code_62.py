def solve():
    a, b, c = map(int, input().split())
    
    best_cost = float('inf')
    best_triple = None
    
    for A in range(1, 2 * a + 1):
        for B in range(A, 2 * b + 1, A):
            for C in range(B, 2 * c + 1, B):
                cost = abs(A - a) + abs(B - b) + abs(C - c)
                if cost < best_cost:
                    best_cost = cost
                    best_triple = (A, B, C)
    
    print(best_cost)
    print(*best_triple)

t = int(input())
for _ in range(t):
    solve()