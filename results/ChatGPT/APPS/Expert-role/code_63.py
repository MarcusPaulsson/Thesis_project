def maximum_happiness(test_cases):
    results = []
    for n, k, a, w in test_cases:
        a.sort()
        w.sort()

        # Calculate the sum of happiness
        happiness_sum = 0
        
        # Friends will get the largest elements
        # Max happiness = max + min, so we start with the largest for max and smallest for min
        for i in range(k):
            happiness_sum += a[-(w[k - i - 1])]  # max value for the i-th friend
            happiness_sum += a[i]                  # min value for the i-th friend
        
        results.append(happiness_sum)

    return results


# Input reading
import sys
input = sys.stdin.read
data = input().splitlines()

idx = 0
t = int(data[idx])
idx += 1
test_cases = []

for _ in range(t):
    n, k = map(int, data[idx].split())
    idx += 1
    a = list(map(int, data[idx].split()))
    idx += 1
    w = list(map(int, data[idx].split()))
    idx += 1
    test_cases.append((n, k, a, w))

# Get results
results = maximum_happiness(test_cases)

# Output results
for res in results:
    print(res)