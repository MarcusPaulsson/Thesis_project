def min_cost_to_obtain_set(n, k, s):
    from collections import Counter
    
    # Count the frequency of each character
    freq = Counter(s)
    
    # Calculate the total number of unique subsequences
    unique_subsequences = 0
    total_cost = 0
    
    # We can generate subsequences of different lengths
    for length in range(1, n + 1):
        # Calculate the number of unique subsequences of this length
        # Using the formula: C(n, length) = n! / (length! * (n - length)!)
        # We can use a simple combinatorial approach to count unique subsequences
        # by considering the frequency of characters.
        
        # For each character, we can choose to include it or not
        # Hence, the number of unique subsequences is 2^count - 1 for each character count
        # But we need to consider the length of subsequences
        
        # Count how many unique subsequences we can form of this length
        count = 0
        for char, count_char in freq.items():
            if count_char >= length:
                count += 1
        
        # If we can form subsequences of this length
        if count > 0:
            unique_subsequences += count
            total_cost += (n - length) * count
        
        # If we have reached or exceeded k unique subsequences, we can stop
        if unique_subsequences >= k:
            return total_cost
    
    # If we exit the loop and have not reached k unique subsequences
    return -1

# Input reading
n, k = map(int, input().split())
s = input().strip()

# Get the result
result = min_cost_to_obtain_set(n, k, s)

# Output the result
print(result)