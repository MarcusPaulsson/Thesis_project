def find_max_subsequence(test_cases):
    results = []
    
    for n, p in test_cases:
        # Initialize the subsequence
        subsequence = []
        
        # Start with the first element
        subsequence.append(p[0])
        
        # Iterate through the permutation
        for i in range(1, n):
            if abs(p[i] - subsequence[-1]) > 1:
                subsequence.append(p[i])
        
        # Check if we need at least two elements
        if len(subsequence) < 2:
            subsequence.append(p[1])  # Guarantee at least two elements
        
        results.append((len(subsequence), subsequence))
    
    return results

# Read input
t = int(input())
test_cases = []

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    test_cases.append((n, p))

# Find results
results = find_max_subsequence(test_cases)

# Output results
for k, subseq in results:
    print(k)
    print(" ".join(map(str, subseq)))