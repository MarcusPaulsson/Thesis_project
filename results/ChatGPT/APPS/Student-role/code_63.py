def max_happiness(t, test_cases):
    results = []
    for case in test_cases:
        n, k, a, w = case
        a.sort()
        w.sort(reverse=True)

        total_happiness = 0
        # Assign the maximum elements to the friends according to their weights
        total_happiness += a[-1] * k  # Each friend gets their own maximum
        # Each friend gets their minimum based on the weights
        for i in range(k):
            total_happiness += a[-(w[i] + 1)]  # Assign the minimum from the remaining highest values

        results.append(total_happiness)
    
    return results

# Reading input
import sys
input = sys.stdin.read
data = input().splitlines()

index = 0
t = int(data[index])
index += 1
test_cases = []

for _ in range(t):
    n, k = map(int, data[index].split())
    index += 1
    a = list(map(int, data[index].split()))
    index += 1
    w = list(map(int, data[index].split()))
    index += 1
    test_cases.append((n, k, a, w))

results = max_happiness(t, test_cases)

# Output the results
for result in results:
    print(result)