def min_operations_to_alternating(t, test_cases):
    results = []
    for n, s in test_cases:
        count_01 = count_10 = 0
        for i in range(n):
            expected_char = '0' if i % 2 == 0 else '1'
            if s[i] != expected_char:
                count_01 += 1
        for i in range(n):
            expected_char = '1' if i % 2 == 0 else '0'
            if s[i] != expected_char:
                count_10 += 1
        
        # Minimum number of operations needed to make the string alternating
        results.append(min(count_01, count_10) // 2)
    
    return results

# Input reading section
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    s = input().strip()
    test_cases.append((n, s))

# Get results
results = min_operations_to_alternating(t, test_cases)

# Output results
for res in results:
    print(res)