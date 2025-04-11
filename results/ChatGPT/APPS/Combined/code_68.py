def min_cost_to_obtain_set(n, k, s):
    from collections import Counter

    # Count the frequency of each character in the string
    freq = Counter(s)
    
    total_cost = 0
    unique_subsequences = 0

    # Iterate over possible lengths of subsequences
    for length in range(1, n + 1):
        current_length_subsequences = sum(1 for count in freq.values() if count >= length)

        if current_length_subsequences == 0:
            break
        
        # Each subsequence of this length has a cost of (n - length)
        total_cost += current_length_subsequences * (n - length)
        unique_subsequences += current_length_subsequences
        
        # Check if we have reached the required size k
        if unique_subsequences >= k:
            return total_cost
    
    # If we exit the loop and haven't reached k unique subsequences, it's impossible
    return -1

# Input reading
n, k = map(int, input().split())
s = input().strip()

# Output the result
print(min_cost_to_obtain_set(n, k, s))