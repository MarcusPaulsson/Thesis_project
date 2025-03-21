def solve():
    import sys
    from collections import defaultdict
    
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        a = list(map(int, data[index:index+n]))
        index += n
        
        # This will hold the last occurrence index of each number
        last_occurrence = defaultdict(lambda: -1)
        
        # This will hold the minimum values for each k
        k_amazing = [-1] * n
        
        # We will iterate through the array to determine the k-amazing numbers
        for i in range(n):
            num = a[i]
            if last_occurrence[num] != -1:
                # Update the distance between the current and last occurrence
                distance = i - last_occurrence[num]
                # We update the k-amazing number only for valid distances
                if distance <= n:
                    # The minimum number that can be the k-amazing number
                    k_amazing[distance-1] = max(k_amazing[distance-1], num)
            # Update the last occurrence of the current number
            last_occurrence[num] = i
        
        # Handle the numbers in reverse to ensure we propagate the minimum down
        for k in range(n-2, -1, -1):
            k_amazing[k] = max(k_amazing[k], k_amazing[k+1])
        
        # Collect results
        for k in range(n):
            k_amazing[k] = k_amazing[k] if k_amazing[k] != -1 else -1
        
        results.append(" ".join(map(str, k_amazing)))
    
    print("\n".join(results))

# Uncomment the line below to run the solve function
# solve()