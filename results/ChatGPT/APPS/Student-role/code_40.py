def min_operations_to_sort(q, queries):
    results = []
    
    for n, a in queries:
        # Count frequency of each element
        from collections import Counter
        count = Counter(a)
        
        # Create a sorted version of the array
        sorted_a = sorted(a)
        
        # Find the longest prefix of the sorted array that can be formed
        max_length = 0
        current_length = 0
        
        for i in range(n):
            if i == 0 or sorted_a[i] == sorted_a[i-1]:
                current_length += count[sorted_a[i]]
            else:
                # Reset the current length for new element
                max_length = max(max_length, current_length)
                current_length = count[sorted_a[i]]
        
        # Final check for the last element
        max_length = max(max_length, current_length)
        
        # Minimum operations needed is total elements minus the size of the longest valid prefix
        min_operations = n - max_length
        results.append(min_operations)
    
    return results

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

q = int(data[0])
queries = []

index = 1
for _ in range(q):
    n = int(data[index])
    a = list(map(int, data[index + 1].split()))
    queries.append((n, a))
    index += 2

# Get results
results = min_operations_to_sort(q, queries)

# Print results
for result in results:
    print(result)