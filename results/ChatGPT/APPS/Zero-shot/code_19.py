def check_records(test_cases):
    results = []
    for case in test_cases:
        n = case[0]
        pairs = case[1]
        valid = True
        
        for i in range(n):
            p, c = pairs[i]
            if i > 0:
                prev_p, prev_c = pairs[i - 1]
                if p < prev_p or c < prev_c or c > p:
                    valid = False
                    break
                if (p - prev_p) < (c - prev_c):
                    valid = False
                    break
        
        if valid:
            results.append("YES")
        else:
            results.append("NO")
    
    return results

# Read input
T = int(input())
test_cases = []
for _ in range(T):
    n = int(input())
    pairs = [tuple(map(int, input().split())) for _ in range(n)]
    test_cases.append((n, pairs))

# Check each test case and print results
results = check_records(test_cases)
print("\n".join(results))