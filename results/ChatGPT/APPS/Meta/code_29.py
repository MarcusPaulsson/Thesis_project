def min_replacements_to_lucky(ticket):
    # Split the ticket into two halves
    first_half = list(map(int, ticket[:3]))
    second_half = list(map(int, ticket[3:]))
    
    # Calculate the sums of both halves
    sum_first = sum(first_half)
    sum_second = sum(second_half)
    
    # Calculate the difference
    diff = abs(sum_first - sum_second)
    
    # If the ticket is already lucky
    if diff == 0:
        return 0
    
    # Create a list of possible changes
    changes = []
    for digit in first_half:
        changes.append(9 - digit)  # Max change possible for first half
    for digit in second_half:
        changes.append(digit)  # Max change possible for second half
    
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