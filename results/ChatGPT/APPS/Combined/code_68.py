def min_cost_to_obtain_set(n, k, s):
    from collections import Counter

    # Count the frequency of each character in the string
    char_count = Counter(s)
    
    # Calculate the maximum number of unique subsequences we can create
    unique_counts = []
    
    for length in range(1, n + 1):
        count_of_length = sum(1 for char in char_count if char_count[char] >= length)
        if count_of_length > 0:
            unique_counts.append(count_of_length)
    
    total_unique_count = sum(unique_counts)

    # Step 3: Check if it's possible to get k unique subsequences
    if total_unique_count < k:
        return -1

    # Step 4: Calculate the minimum cost
    total_cost = 0
    remaining_k = k

    # Iterate through potential lengths of subsequences
    for length in range(n + 1):
        if remaining_k <= 0:
            break
        
        count_of_length = unique_counts[length] if length < len(unique_counts) else 0
        if count_of_length > 0:
            if remaining_k >= count_of_length:
                total_cost += (n - length) * count_of_length
                remaining_k -= count_of_length
            else:
                total_cost += (n - length) * remaining_k
                remaining_k = 0

    return total_cost

# Input reading
n, k = map(int, input().split())
s = input().strip()

# Output the result
print(min_cost_to_obtain_set(n, k, s))