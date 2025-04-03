def min_replacements_to_lucky(ticket):
    first_half = list(map(int, ticket[:3]))
    second_half = list(map(int, ticket[3:]))
    
    sum_first = sum(first_half)
    sum_second = sum(second_half)
    
    if sum_first == sum_second:
        return 0
    
    # Calculate the differences
    diff = abs(sum_first - sum_second)
    
    # Create a list of possible changes
    changes = []
    if sum_first > sum_second:
        # We need to decrease the first half or increase the second half
        changes += [digit for digit in first_half]
        changes += [9 - digit for digit in second_half]
    else:
        # We need to decrease the second half or increase the first half
        changes += [digit for digit in second_half]
        changes += [9 - digit for digit in first_half]
    
    # Sort changes in descending order
    changes.sort(reverse=True)

    # Calculate the minimum replacements needed
    count = 0
    for change in changes:
        diff -= change
        count += 1
        if diff <= 0:
            break
    
    return count

# Example usage
ticket = input().strip()
print(min_replacements_to_lucky(ticket))