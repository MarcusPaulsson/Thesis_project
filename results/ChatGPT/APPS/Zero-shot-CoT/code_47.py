def max_strength_of_army(test_cases):
    results = []
    
    for n, a in test_cases:
        # Calculate the maximum alternating sum
        max_strength = 0
        
        # We want to maximize the sum of the form:
        # a[b1] - a[b2] + a[b3] - a[b4] + ...
        # To achieve this, we want to pick the largest numbers in odd positions 
        # and the smallest numbers in even positions.
        
        # Sort the array to easily pick largest and smallest values
        sorted_a = sorted(a)
        
        # we will pick from the end for max values and from the start for min values
        odd_index_sum = 0
        even_index_sum = 0
        
        # Choose the largest elements for odd indices and smallest for even indices
        for i in range(n):
            if i % 2 == 0:  # odd indices in terms of 1-based (0, 2, 4... in 0-based)
                odd_index_sum += sorted_a[n - 1 - (i // 2)]
            else:           # even indices in terms of 1-based (1, 3, 5... in 0-based)
                even_index_sum += sorted_a[i // 2]
        
        max_strength = odd_index_sum - even_index_sum
        results.append(max_strength)
    
    return results

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
test_cases = []

index = 1
for _ in range(t):
    n, q = map(int, data[index].split())
    a = list(map(int, data[index + 1].split()))
    test_cases.append((n, a))
    index += 2

# Get the results
results = max_strength_of_army(test_cases)

# Print the results
for result in results:
    print(result)