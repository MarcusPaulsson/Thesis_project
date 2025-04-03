def count_exterminable_subarrays(q, queries):
    results = []
    
    for n, a in queries:
        count = 0
        # To store the last index of each element
        last_index = {}
        # To store the current stack's size
        stack = []
        
        # Iterate over each end index of the subarray
        for end in range(n):
            # If the stack is not empty and the top element is the same as the current
            if stack and stack[-1] == a[end]:
                stack.pop()  # Pop the top element
            else:
                stack.append(a[end])  # Push new element
            
            # Check for exterminable subarrays ending at 'end'
            if not stack:  # If stack is empty
                count += end + 1  # All subarrays from the start to 'end' are valid
            
            # Check for pairs that can form exterminable subarrays
            if a[end] in last_index:
                last_pos = last_index[a[end]]
                if last_pos != -1:  # If there is a valid previous position
                    count += (last_pos + 1)  # Add the number of valid subarrays ending at this position
            
            last_index[a[end]] = end  # Update the last index of the current element
        
        results.append(count)
    
    return results

# Read input
import sys
input = sys.stdin.read
data = input().split()

index = 0
q = int(data[index])
index += 1
queries = []

for _ in range(q):
    n = int(data[index])
    index += 1
    a = list(map(int, data[index:index + n]))
    index += n
    queries.append((n, a))

# Get the results
results = count_exterminable_subarrays(q, queries)

# Print the results
for result in results:
    print(result)