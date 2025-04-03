def max_operations(t, cases):
    results = []
    for n, s in cases:
        count = 0
        current_char = ''
        for char in s:
            if char != current_char:
                count += 1
                current_char = char
        results.append(count)
    return results

# Input reading
t = int(input())
cases = []
for _ in range(t):
    n = int(input())
    s = input().strip()
    cases.append((n, s))

# Get results
results = max_operations(t, cases)

# Output results
for result in results:
    print(result)