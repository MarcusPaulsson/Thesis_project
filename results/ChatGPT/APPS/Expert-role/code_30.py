def min_operations_to_alternating(t, test_cases):
    results = []
    for n, s in test_cases:
        # Count the number of mismatches for both patterns
        pattern1_mismatches = sum(1 for i in range(n) if s[i] != '01'[(i % 2)])
        pattern2_mismatches = sum(1 for i in range(n) if s[i] != '10'[(i % 2)])
        
        # The number of operations needed is half the number of mismatches
        min_operations = min(pattern1_mismatches, pattern2_mismatches) // 2
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

# Print results
for result in results:
    print(result)