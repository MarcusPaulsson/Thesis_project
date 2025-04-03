def min_operations_to_sort(q, queries):
    results = []
    for i in range(q):
        n = queries[i][0]
        a = queries[i][1]
        
        # Count frequency of each number and their positions
        from collections import defaultdict
        
        freq = defaultdict(int)
        for number in a:
            freq[number] += 1
        
        # Create a sorted version of the array
        sorted_a = sorted(a)
        
        # Find the longest prefix of the sorted array that matches the original array
        longest_prefix = 0
        count = defaultdict(int)
        
        for j in range(n):
            if count[sorted_a[j]] < freq[sorted_a[j]]:
                count[sorted_a[j]] += 1
                longest_prefix += 1
        
        # The minimum operations needed is the number of unique elements minus the longest prefix
        unique_elements = len(freq)
        min_operations = unique_elements - longest_prefix
        
        results.append(str(min_operations))
    
    return "\n".join(results)

# Reading input
import sys
input = sys.stdin.read
data = input().splitlines()

q = int(data[0])
queries = []
line_index = 1

for _ in range(q):
    n = int(data[line_index])
    a = list(map(int, data[line_index + 1].split()))
    queries.append((n, a))
    line_index += 2

# Get results and print them
output = min_operations_to_sort(q, queries)
print(output)