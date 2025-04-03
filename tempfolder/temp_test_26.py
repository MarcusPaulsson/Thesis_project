def can_solve_puzzle(n, m):
    return (n % 2 == 0 and m % 2 == 0) or (n % 2 == 1 and m % 2 == 1)

t = int(input())
results = []
for _ in range(t):
    n, m = map(int, input().split())
    if can_solve_puzzle(n, m):
        results.append("YES")
    else:
        results.append("NO")

print("\n".join(results))