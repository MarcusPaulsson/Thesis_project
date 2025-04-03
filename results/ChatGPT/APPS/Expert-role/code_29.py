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
        # We want to reduce the sum of the first half or increase the sum of the second half
        changes = [9 - d for d in first_half] + [d for d in second_half]
    else:
        # We want to reduce the sum of the second half or increase the sum of the first half
        changes = [9 - d for d in second_half] + [d for d in first_half]
    
    # Sort changes in descending order
    changes.sort(reverse=True)
    
    count = 0
    for change in changes:
        diff -= change
        count += 1
        if diff <= 0:
            return count
    
    return count

# Read input
ticket = input().strip()
# Output result
print(min_replacements_to_lucky(ticket))