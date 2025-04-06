def solve():
    a, b, c = map(int, input().split())
    
    best_cost = float('inf')
    best_abc = None
    
    for A in range(1, 2 * a + 1):
        for B in range(A, 2 * b + 1, A):
            C1 = (c // B) * B
            C2 = C1 + B
            
            if C1 > 0:
                cost1 = abs(A - a) + abs(B - b) + abs(C1 - c)
                if cost1 < best_cost:
                    best_cost = cost1
                    best_abc = (A, B, C1)
            
            if C2 > 0 and C2 <= 3*c:
                cost2 = abs(A - a) + abs(B - b) + abs(C2 - c)
                if cost2 < best_cost:
                    best_cost = cost2
                    best_abc = (A, B, C2)

    print(best_cost)
    print(*best_abc)

t = int(input())
for _ in range(t):
    solve()