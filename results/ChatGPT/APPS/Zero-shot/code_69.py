def check_records(test_cases):
    results = []
    for case in test_cases:
        n, stats = case
        correct = True
        for i in range(1, n):
            p_prev, c_prev = stats[i - 1]
            p_curr, c_curr = stats[i]

            if p_curr < p_prev or c_curr < c_prev or c_curr > p_curr:
                correct = False
                break
            
            # Check if the increase in clears is valid
            if c_curr - c_prev > p_curr - p_prev:
                correct = False
                break
            
        results.append("YES" if correct else "NO")
    
    return results

# Read input
T = int(input())
test_cases = []
for _ in range(T):
    n = int(input())
    stats = [tuple(map(int, input().split())) for _ in range(n)]
    test_cases.append((n, stats))

# Check records for each test case and print results
results = check_records(test_cases)
for result in results:
    print(result)