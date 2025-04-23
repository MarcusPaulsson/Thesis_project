def color_array(n, k, a):
    from collections import defaultdict
    
    # Step 1: Count occurrences of each number
    count = defaultdict(int)
    for num in a:
        count[num] += 1
    
    # Step 2: Check if any number occurs more than k times
    if any(c > k for c in count.values()):
        return "NO"
    
    # Step 3: Prepare to assign colors
    color_assignment = [0] * n
    color_used = defaultdict(int)
    
    # Step 4: Assign colors
    for i in range(n):
        num = a[i]
        color_used[num] += 1
        color_assignment[i] = color_used[num] % k or k  # Ensure color is in the range [1, k]
    
    return "YES", color_assignment

# Input reading
n, k = map(int, input().split())
a = list(map(int, input().split()))

# Get the result
result = color_array(n, k, a)

# Output the result
if result == "NO":
    print(result)
else:
    print(result[0])
    print(' '.join(map(str, result[1])))