def min_replacements(ticket):
    first_half = list(map(int, ticket[:3]))
    second_half = list(map(int, ticket[3:]))
    
    sum_first = sum(first_half)
    sum_second = sum(second_half)
    
    if sum_first == sum_second:
        return 0
    
    # Calculate the difference between the sums
    diff = abs(sum_first - sum_second)
    
    # Create lists of the potential gains from changing digits
    if sum_first > sum_second:
        # We need to reduce sum_first or increase sum_second
        changes = sorted([9 - d for d in first_half] + [d for d in second_half], reverse=True)
    else:
        # We need to reduce sum_second or increase sum_first
        changes = sorted([9 - d for d in second_half] + [d for d in first_half], reverse=True)
    
    # Determine the minimum number of changes needed
    count = 0
    for change in changes:
        diff -= change
        count += 1
        if diff <= 0:
            return count
    
    return count  # In case we don't reach the required balance

# Example usage
ticket = input().strip()
print(min_replacements(ticket))