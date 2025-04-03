def maximize_happiness(t, test_cases):
    results = []
    for case in test_cases:
        n, k, a, w = case
        a.sort()
        w.sort()
        
        happiness_sum = 0
        
        # Calculate the happiness contribution of the largest elements
        for i in range(k):
            happiness_sum += a[n - w[k - 1 - i]]  # max element for each friend
        
        # Calculate the happiness contribution of the smallest elements
        for i in range(k - 1):
            happiness_sum += a[i]  # min element for each friend
        
        results.append(happiness_sum)
        
    return results

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
index = 1
test_cases = []
for _ in range(t):
    n, k = map(int, data[index].split())
    index += 1
    a = list(map(int, data[index].split()))
    index += 1
    w = list(map(int, data[index].split()))
    index += 1
    
    test_cases.append((n, k, a, w))

# Get results
results = maximize_happiness(t, test_cases)

# Print results
for result in results:
    print(result)