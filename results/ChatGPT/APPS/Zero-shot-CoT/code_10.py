def find_maximum_subsequence(t, test_cases):
    results = []
    
    for n, p in test_cases:
        # Initialize variables to store the best subsequence
        best_subsequence = []
        
        # We will always take the first and last element of the permutation
        best_subsequence.append(p[0])
        best_subsequence.append(p[-1])
        
        # Append the result for this test case
        results.append((len(best_subsequence), best_subsequence))
    
    return results

# Reading input
import sys
input = sys.stdin.read
data = input().splitlines()
t = int(data[0])
test_cases = []

line_index = 1
for _ in range(t):
    n = int(data[line_index])
    p = list(map(int, data[line_index + 1].split()))
    test_cases.append((n, p))
    line_index += 2

# Finding the results
results = find_maximum_subsequence(t, test_cases)

# Outputting results
output = []
for k, subsequence in results:
    output.append(f"{k}")
    output.append(" ".join(map(str, subsequence)))

print("\n".join(output))