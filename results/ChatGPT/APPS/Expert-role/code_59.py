def minimize_difference(t, test_cases):
    results = []
    for i in range(t):
        n, a = test_cases[i]
        min_value = float('inf')
        max_value = float('-inf')

        for value in a:
            if value != -1:
                min_value = min(min_value, value)
                max_value = max(max_value, value)

        # k can be chosen between min_value and max_value
        k = (min_value + max_value) // 2
        m = max(abs(k - min_value), abs(k - max_value))

        results.append((m, k))

    return results


# Input reading
import sys
input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
test_cases = []

index = 1
for _ in range(t):
    n = int(data[index])
    a = list(map(int, data[index + 1].split()))
    test_cases.append((n, a))
    index += 2

results = minimize_difference(t, test_cases)

# Output results
for m, k in results:
    print(m, k)