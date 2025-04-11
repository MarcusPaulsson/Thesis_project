def min_replacements_to_lucky(ticket):
    first_half = list(map(int, ticket[:3]))
    second_half = list(map(int, ticket[3:]))
    
    sum_first = sum(first_half)
    sum_second = sum(second_half)
    
    if sum_first == sum_second:
        return 0
    
    # Calculate the difference
    diff = abs(sum_first - sum_second)
    
    # Create a list of possible changes
    changes = []
    if sum_first > sum_second:
        # We need to decrease the first half or increase the second half
        changes.extend([9 - d for d in first_half])  # Maximize decrease from first half
        changes.extend([d for d in second_half])     # Maximize increase from second half
    else:
        # We need to decrease the second half or increase the first half
        changes.extend([9 - d for d in second_half]) # Maximize decrease from second half
        changes.extend([d for d in first_half])      # Maximize increase from first half
    
    # Sort changes in descending order
    changes.sort(reverse=True)
    
    # Calculate the minimum number of replacements needed
    replacements = 0
    for change in changes:
        diff -= change
        replacements += 1
        if diff <= 0:
            break
    
    return replacements

# Example usage
ticket = input().strip()
print(min_replacements_to_lucky(ticket))