def min_replacements_to_lucky(ticket: str) -> int:
    # Split the ticket into two halves and convert to integers
    first_half = list(map(int, ticket[:3]))
    second_half = list(map(int, ticket[3:]))
    
    # Calculate the sums of both halves
    sum_first = sum(first_half)
    sum_second = sum(second_half)
    
    # Calculate the difference
    difference = abs(sum_first - sum_second)
    
    # If the sums are already equal, no replacements are needed
    if difference == 0:
        return 0
    
    # Create a list of possible changes (max change per digit)
    changes = []
    if sum_first < sum_second:
        # Need to increase the first half or decrease the second half
        changes.extend(9 - digit for digit in first_half)  # Max increase for first half
        changes.extend(digit for digit in second_half)     # Max decrease for second half
    else:
        # Need to decrease the first half or increase the second half
        changes.extend(digit for digit in first_half)      # Max decrease for first half
        changes.extend(9 - digit for digit in second_half) # Max increase for second half
    
    # Sort changes in descending order to maximize the effect of each change
    changes.sort(reverse=True)
    
    # Calculate the minimum number of replacements needed
    replacements = 0
    for change in changes:
        difference -= change
        replacements += 1
        if difference <= 0:
            break
    
    return replacements

# Example usage
ticket = input().strip()
print(min_replacements_to_lucky(ticket))