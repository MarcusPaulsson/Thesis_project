def find_max_subsequence(t, test_cases):
    results = []
    
    for n, p in test_cases:
        # We will collect the points where the value changes significantly
        subsequence = [p[0]]
        
        for i in range(1, n):
            if abs(p[i] - p[i - 1]) > 1:
                subsequence.append(p[i])
        
        if len(subsequence) < 2:
            subsequence = [p[0], p[-1]]  # Fallback if we have no sufficient changes
        
        results.append(f"{len(subsequence)}\n{' '.join(map(str, subsequence))}")
    
    return "\n".join(results)

# Reading input
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

# Getting results
output = find_max_subsequence(t, test_cases)
print(output)