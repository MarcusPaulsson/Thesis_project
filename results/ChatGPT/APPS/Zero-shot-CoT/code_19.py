def check_records(test_cases):
    results = []
    for case in test_cases:
        n, stats = case
        valid = True
        for i in range(n):
            p_i, c_i = stats[i]
            if i > 0:
                p_prev, c_prev = stats[i - 1]
                if p_i < p_prev or c_i < c_prev or c_i > p_i:
                    valid = False
                    break
                if c_i - c_prev > p_i - p_prev:
                    valid = False
                    break
        results.append("YES" if valid else "NO")
    return results

# Read input
T = int(input())
test_cases = []
for _ in range(T):
    n = int(input())
    stats = [tuple(map(int, input().split())) for _ in range(n)]
    test_cases.append((n, stats))

# Get results and print
results = check_records(test_cases)
for result in results:
    print(result)