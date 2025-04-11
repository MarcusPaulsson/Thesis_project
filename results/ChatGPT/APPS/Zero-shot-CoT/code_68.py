def min_cost_to_obtain_set(n, k, s):
    from collections import Counter
    
    # Count the frequency of each character in the string
    freq = Counter(s)
    
    # Calculate the number of distinct subsequences we can generate
    distinct_subsequences = 0
    total_cost = 0
    
    # We can generate subsequences of different lengths
    for length in range(1, n + 1):
        # Calculate the number of distinct subsequences of this length
        # Using the formula: C(n, r) = n! / (r! * (n - r)!)
        # We can use a simple approach to count distinct subsequences
        # by considering the frequency of characters
        count = 1
        for char, count_char in freq.items():
            count *= (count_char + 1)  # +1 for choosing 0 to count_char of this character
        count -= 1  # Subtract the empty subsequence
        
        if distinct_subsequences + count >= k:
            # We can reach or exceed k with this length
            total_cost += (n - length) * (k - distinct_subsequences)
            return total_cost
        else:
            # Add all distinct subsequences of this length
            total_cost += (n - length) * count
            distinct_subsequences += count
    
    # If we exit the loop and have not reached k, it's impossible
    return -1

# Read input
n, k = map(int, input().split())
s = input().strip()

# Get the result
result = min_cost_to_obtain_set(n, k, s)

# Print the result
print(result)