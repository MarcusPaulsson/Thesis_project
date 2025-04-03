def count_exterminable_subarrays(q, queries):
    results = []
    
    for n, a in queries:
        # To keep track of the last positions of elements
        last_position = {}
        # To keep the count of exterminable subarrays
        exterminable_count = 0
        # Using a stack to simulate the extermination process
        stack = []
        
        for i in range(n):
            # Check if the current element is the same as the top of the stack
            if stack and stack[-1] == a[i]:
                stack.pop()  # Pop the top element
            else:
                stack.append(a[i])  # Push current element
            
            # Check if the stack is empty which means subarray ending at i is exterminable
            if not stack:
                exterminable_count += (i + 1)  # All subarrays ending at i are exterminable
            
            # Check for the case of previous elements
            # If the current element has appeared before, we need to adjust the exterminable count
            if a[i] in last_position:
                # The last position of this element
                last_idx = last_position[a[i]]
                # The number of exterminable subarrays is reduced by the count of subarrays
                # ending at previous index of the same element
                exterminable_count -= (last_idx + 1)
            
            # Update the last position of the current element
            last_position[a[i]] = i
        
        results.append(exterminable_count)
    
    return results

# Input reading
import sys
input = sys.stdin.read
data = input().split()

q = int(data[0])
index = 1
queries = []

for _ in range(q):
    n = int(data[index])
    index += 1
    a = list(map(int, data[index:index + n]))
    index += n
    queries.append((n, a))

# Get results
results = count_exterminable_subarrays(q, queries)

# Print outputs
for result in results:
    print(result)