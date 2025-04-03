def min_operations_to_sort(q, queries):
    results = []
    
    for n, a in queries:
        # Frequency map to count occurrences of each number
        freq = {}
        for num in a:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        # Create a list of unique numbers sorted
        unique_sorted = sorted(freq.keys())
        
        # Create a map to count the longest prefix that matches the sorted order
        prefix_count = 0
        current_index = 0
        
        # Traverse the original array to build the prefix count
        for num in a:
            if current_index < len(unique_sorted) and num == unique_sorted[current_index]:
                prefix_count += 1
                if prefix_count == freq[num]:
                    current_index += 1
        
        # The minimum operations needed to sort the array
        min_operations = len(unique_sorted) - prefix_count
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
print('\n'.join(map(str, results)))