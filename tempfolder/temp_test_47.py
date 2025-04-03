def max_strength(n, a):
    # Initialize variables for maximum strength calculation
    max_strength = 0
    
    # Iterate through the elements of the array
    for i in range(n):
        # Add the current element if it is at an odd index (1-based)
        if i % 2 == 0:
            max_strength += a[i]
        # Subtract the current element if it is at an even index (1-based)
        else:
            max_strength -= a[i]
    
    return max_strength

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
index = 1
results = []

for _ in range(t):
    n, q = map(int, data[index].split())
    index += 1
    a = list(map(int, data[index].split()))
    index += 1
    
    # Calculate the maximum strength for the current test case
    result = max_strength(n, sorted(a))
    results.append(result)

# Print all results
print("\n".join(map(str, results)))