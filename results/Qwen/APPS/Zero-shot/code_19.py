def check_records(T, test_cases):
    results = []
    for n, pairs in test_cases:
        p_prev, c_prev = pairs[0]
        valid = True
        for i in range(1, n):
            p_curr, c_curr = pairs[i]
            if p_curr < p_prev or c_curr < c_prev or c_curr > p_curr:
                valid = False
                break
            p_prev, c_prev = p_curr, c_curr
        results.append("YES" if valid else "NO")
    return results

# Read input
T = int(input())
test_cases = []
for _ in range(T):
    n = int(input())
    pairs = [tuple(map(int, input().split())) for _ in range(n)]
    test_cases.append((n, pairs))

# Check records and print results
results = check_records(T, test_cases)
for result in results:
    print(result)