def count_exterminable_subarrays(q, queries):
    results = []
    
    for n, a in queries:
        count = 0
        stack = []
        last_pos = {}
        
        # To track the last position of each number
        for i in range(n):
            if a[i] in last_pos:
                last_pos[a[i]].append(i)
            else:
                last_pos[a[i]] = [i]
        
        # To find exterminable subarrays
        for i in range(n):
            if not stack or stack[-1] != a[i]:
                stack.append(a[i])
            else:
                stack.pop()
            
            # Count exterminable subarrays ending at `i`
            # If the stack is empty, it means we found an exterminable subarray
            if not stack:
                count += (i + 1)  # All starting positions from 0 to i are valid
            
            # Now we need to track the last seen position for current stack top
            if stack:
                last_value = stack[-1]
                if last_value in last_pos:
                    # We only consider the last position of the same value
                    for pos in last_pos[last_value]:
                        if pos < i:
                            count += (pos + 1)
                            break
        
        results.append(count)
    
    return results

# Read input
q = int(input().strip())
queries = []

for _ in range(q):
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    queries.append((n, a))

# Get results
results = count_exterminable_subarrays(q, queries)

# Output results
for result in results:
    print(result)