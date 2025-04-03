def min_operations_to_alternate(t, cases):
    results = []
    for n, s in cases:
        count_01 = 0
        count_10 = 0
        
        # Count mismatches for both '01' and '10' patterns
        for i in range(n):
            expected = '0' if i % 2 == 0 else '1'
            if s[i] != expected:  # mismatch with '010101...'
                count_01 += 1
        
        for i in range(n):
            expected = '1' if i % 2 == 0 else '0'
            if s[i] != expected:  # mismatch with '101010...'
                count_10 += 1
        
        # Minimum operations needed
        results.append(min(count_01, count_10) // 2)
    
    return results

# Input reading
t = int(input())
cases = []
for _ in range(t):
    n = int(input())
    s = input().strip()
    cases.append((n, s))

# Calculate results
results = min_operations_to_alternate(t, cases)

# Output results
for result in results:
    print(result)