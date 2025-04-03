def max_operations(t, test_cases):
    results = []
    for n, s in test_cases:
        count = 0
        last_char = ''
        for char in s:
            if char != last_char:
                count += 1
                last_char = char
        results.append(count)
    return results

# Input handling
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    s = input().strip()
    test_cases.append((n, s))

# Get results
results = max_operations(t, test_cases)

# Output results
for result in results:
    print(result)