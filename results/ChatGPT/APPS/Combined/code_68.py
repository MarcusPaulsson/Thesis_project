def min_cost_to_obtain_set(n, k, s):
    # To store unique subsequences and their costs
    unique_subsequences = set()
    total_cost = 0
    
    # Generate all possible subsequences using a bitmask approach
    for i in range(1 << n):  # 2^n possible subsequences
        subsequence = []
        for j in range(n):
            if i & (1 << j):
                subsequence.append(s[j])
        subsequence_str = ''.join(subsequence)
        
        # Add unique subsequences
        if subsequence_str not in unique_subsequences:
            unique_subsequences.add(subsequence_str)
            total_cost += n - len(subsequence_str)  # Calculate cost of the subsequence
            
            # Stop if we have reached the required number of unique subsequences
            if len(unique_subsequences) == k:
                break

    # Check if we have enough unique subsequences
    if len(unique_subsequences) < k:
        return -1

    return total_cost

# Input reading
n, k = map(int, input().split())
s = input().strip()

# Output the result
print(min_cost_to_obtain_set(n, k, s))