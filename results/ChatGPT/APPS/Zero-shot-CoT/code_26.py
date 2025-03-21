def can_solve_puzzle(test_cases):
    results = []
    for n, m in test_cases:
        if (n * m) % 2 == 0:
            results.append("YES")
        else:
            results.append("NO")
    return results

t = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(t)]
results = can_solve_puzzle(test_cases)

for result in results:
    print(result)