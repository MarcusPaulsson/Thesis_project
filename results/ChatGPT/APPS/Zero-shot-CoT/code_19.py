def check_records(test_cases):
    results = []
    for case in test_cases:
        n, stats = case
        valid = True
        for i in range(n):
            p, c = stats[i]
            if i > 0:
                prev_p, prev_c = stats[i - 1]
                if p < prev_p or c < prev_c or c > p:
                    valid = False
                    break
                if (p - prev_p) < (c - prev_c):
                    valid = False
                    break
        results.append("YES" if valid else "NO")
    return results

T = int(input())
test_cases = []
for _ in range(T):
    n = int(input())
    stats = [tuple(map(int, input().split())) for _ in range(n)]
    test_cases.append((n, stats))

results = check_records(test_cases)
for result in results:
    print(result)