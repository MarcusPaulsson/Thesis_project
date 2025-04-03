def min_operations_to_alternating(t, test_cases):
    results = []
    for n, s in test_cases:
        # Count the number of mismatches for the two possible alternating patterns
        pattern1 = '01' * (n // 2)  # alternating starting with '0'
        pattern2 = '10' * (n // 2)  # alternating starting with '1'
        
        mismatch1 = sum(1 for i in range(n) if s[i] != pattern1[i])
        mismatch2 = sum(1 for i in range(n) if s[i] != pattern2[i])
        
        # The minimum number of operations needed
        min_operations = min(mismatch1, mismatch2) // 2
        results.append(min_operations)
    
    return results

# Read input
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    s = input().strip()
    test_cases.append((n, s))

# Get results
results = min_operations_to_alternating(t, test_cases)

# Print output
for result in results:
    print(result)