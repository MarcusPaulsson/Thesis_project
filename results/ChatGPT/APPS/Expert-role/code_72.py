def is_beautiful_array_possible(n, k, a):
    # Dictionary to keep track of the sums of each subarray of length k
    sums = {}
    
    for i in range(n - k + 1):
        current_sum = sum(a[i:i + k])
        # We add the sum into the dictionary with the first element of the subarray as key
        if current_sum in sums:
            sums[current_sum].append(a[i])
        else:
            sums[current_sum] = [a[i]]
    
    # Check if the sums of subarrays of length k are consistent
    if len(sums) > 1:
        return -1  # It's impossible to make the array beautiful
    
    # We can create a beautiful array based on the first unique k elements found
    unique_elements = list(sums.keys())[0]
    beautiful_array = []
    
    # We can repeat the first k unique elements to form a beautiful array
    for i in range(10000 // k):
        beautiful_array.extend(unique_elements)
    
    return (len(beautiful_array), beautiful_array[:10000])

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    result = is_beautiful_array_possible(n, k, a)
    
    if result == -1:
        print(-1)
    else:
        m, beautiful_array = result
        print(m)
        print(' '.join(map(str, beautiful_array)))