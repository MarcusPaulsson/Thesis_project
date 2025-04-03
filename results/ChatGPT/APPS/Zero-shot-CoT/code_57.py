def can_reduce_to_one(t, test_cases):
    results = []
    for n, a in test_cases:
        # Find the maximum value's index
        max_index = a.index(max(a))
        
        # Check if there's an increasing sequence to the left or right of the maximum
        left_increasing = any(a[i] < a[i + 1] for i in range(max_index))
        right_increasing = any(a[i] < a[i + 1] for i in range(max_index, n - 1))
        
        if left_increasing or right_increasing:
            results.append("YES")
        else:
            results.append("NO")
    
    return results

# Reading input
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

# Get results
results = can_reduce_to_one(t, test_cases)

# Output results
print("\n".join(results))