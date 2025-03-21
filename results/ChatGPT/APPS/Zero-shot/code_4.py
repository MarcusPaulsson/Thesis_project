def is_beautiful_permutation(t, test_cases):
    results = []
    for n, p in test_cases:
        beautiful = ['0'] * n
        max_value = 0
        for i in range(n):
            max_value = max(max_value, p[i])
            if max_value == i + 1:
                beautiful[i] = '1'
        results.append(''.join(beautiful))
    return results

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
test_cases = []
index = 1
for _ in range(t):
    n = int(data[index])
    p = list(map(int, data[index + 1].split()))
    test_cases.append((n, p))
    index += 2

# Get results
results = is_beautiful_permutation(t, test_cases)

# Print results
for result in results:
    print(result)