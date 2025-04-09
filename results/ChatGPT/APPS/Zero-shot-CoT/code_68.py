def min_cost_to_form_set(n, k, s):
    from collections import defaultdict

    # Count frequencies of each character in the string
    freq = defaultdict(int)
    for char in s:
        freq[char] += 1
    
    # List of character counts
    count_list = sorted(freq.values(), reverse=True)
    
    total_subsequences = 0
    total_cost = 0

    # We can generate subsequences by choosing characters
    for length in range(n + 1):
        # Each character can contribute to subsequences of this length
        # The number of ways to choose a character from its count is (count + 1)
        # We need to count the number of unique subsequences of length `length`
        current_contributions = 1  # Start with the empty subsequence
        for count in count_list:
            current_contributions *= (count + 1)
            if current_contributions >= k:  # If we exceed k, we only need k
                current_contributions = k
                break
        
        if length == 0:
            # We can always form the empty subsequence
            total_subsequences += 1
            if total_subsequences >= k:
                return total_cost
        
        # Calculate the number of subsequences of this length
        subsequences_of_length = current_contributions
        total_subsequences += subsequences_of_length
        
        # If we have enough unique subsequences
        if total_subsequences >= k:
            # The cost is the number of characters we didn't use
            total_cost += length * (total_subsequences - k)
            return total_cost
        
        # Update the cost for the next round
        total_cost += length * subsequences_of_length
    
    return -1

# Input reading
n, k = map(int, input().split())
s = input().strip()

# Output the result
print(min_cost_to_form_set(n, k, s))