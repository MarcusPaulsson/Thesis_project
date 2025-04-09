def min_cost_to_obtain_set(n, k, s):
    from collections import defaultdict
    
    # Count frequency of each character in the string
    freq = defaultdict(int)
    for char in s:
        freq[char] += 1
    
    # Calculate all unique subsequences and their costs
    unique_subsequences = set()
    total_cost = 0
    max_possible_subsequences = 0
    
    # Generate subsequences using bit masking
    for i in range(1 << n):
        subsequence = []
        for j in range(n):
            if i & (1 << j):
                subsequence.append(s[j])
        subsequence_str = ''.join(subsequence)
        if subsequence_str not in unique_subsequences:
            unique_subsequences.add(subsequence_str)
            cost = n - len(subsequence_str)
            total_cost += cost
            max_possible_subsequences += 1
            
            if max_possible_subsequences >= k:
                return total_cost
    
    # If we can't create enough unique subsequences
    if max_possible_subsequences < k:
        return -1
    
    return total_cost

# Read inputs
n, k = map(int, input().split())
s = input().strip()

# Get the result and print it
result = min_cost_to_obtain_set(n, k, s)
print(result)