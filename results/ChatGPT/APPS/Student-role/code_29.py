def min_replacements(ticket):
    first_half = list(map(int, ticket[:3]))
    second_half = list(map(int, ticket[3:]))
    
    sum_first = sum(first_half)
    sum_second = sum(second_half)
    
    if sum_first == sum_second:
        return 0
    
    # Calculate the difference
    diff = abs(sum_first - sum_second)
    
    # Create lists of possible changes
    changes_first = sorted([9 - d for d in first_half], reverse=True)
    changes_second = sorted([9 - d for d in second_half], reverse=True)
    
    # Combine the changes and sort in descending order
    changes = changes_first + changes_second
    changes.sort(reverse=True)
    
    # Determine the minimum number of changes needed
    replacements = 0
    for change in changes:
        diff -= change
        replacements += 1
        if diff <= 0:
            return replacements
    
    return replacements

# Read input
ticket = input().strip()
# Output the result
print(min_replacements(ticket))