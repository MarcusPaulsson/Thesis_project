def min_operations_to_sort(q, queries):
    results = []
    for n, a in queries:
        # Count occurrences of each element
        count = {}
        for num in a:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        # Create a sorted version of the array
        sorted_a = sorted(a)

        # Find the longest prefix of the sorted array that matches
        # with the original array
        left_match = 0
        while (left_match < n and 
               a[left_match] == sorted_a[left_match]):
            left_match += 1

        # Find the longest suffix of the sorted array that matches
        # with the original array
        right_match = 0
        while (right_match < n and 
               a[n - 1 - right_match] == sorted_a[n - 1 - right_match]):
            right_match += 1

        # If the whole array matches, no operations are needed
        if left_match + right_match >= n:
            results.append(0)
        else:
            # Minimum operations needed would be to move the
            # unmatched elements either to the beginning or the end
            results.append(2)

    return results

# Input reading
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

# Get results and print
results = min_operations_to_sort(q, queries)
print('\n'.join(map(str, results)))