def min_cost_to_obtain_set(n, k, s):
    from collections import Counter

    # Count frequencies of each character
    freq = Counter(s)
    
    # Count how many distinct subsequences we can generate
    subseq_count = 0
    cost = 0
    total_cost = 0
    
    # We will keep track of how many subsequences we can generate
    for length in range(n + 1):  # Consider all lengths from 0 to n
        # Calculate how many subsequences of this length we can create
        # The number of distinct subsequences of a given length can be calculated as:
        # 2^(number of distinct characters) - 1 (the empty subsequence)
        # But we need to consider not exceeding k
        if length > 0:
            current_subseq_count = 1
            for count in freq.values():
                current_subseq_count *= (count + 1)  # Each character can be used 0 to count times
            
            current_subseq_count -= 1  # Exclude the empty subsequence
            
            if subseq_count + current_subseq_count >= k:
                # We can fulfill the requirement of k subsequences
                remaining_needed = k - subseq_count
                total_cost += remaining_needed * (n - length)
                break
            else:
                # Accumulate the cost for all subsequences of this length
                total_cost += current_subseq_count * (n - length)
                subseq_count += current_subseq_count

    # If we exit the loop and have not reached k subsequences
    if subseq_count < k:
        return -1
    
    return total_cost


# Read input
n, k = map(int, input().split())
s = input().strip()

# Get the result and print it
result = min_cost_to_obtain_set(n, k, s)
print(result)