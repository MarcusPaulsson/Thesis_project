def min_replacements_to_lucky(ticket):
    # Split the ticket into two halves
    first_half = list(map(int, ticket[:3]))
    second_half = list(map(int, ticket[3:]))
    
    # Calculate the sums of the two halves
    sum_first = sum(first_half)
    sum_second = sum(second_half)
    
    # If ticket is already lucky
    if sum_first == sum_second:
        return 0
    
    # Calculate the difference
    diff = abs(sum_first - sum_second)
    
    # Create a list of possible changes we can make
    changes = []
    
    # Calculate the maximum possible changes for first half
    if sum_first < sum_second:
        for digit in first_half:
            changes.append(9 - digit)  # Max we can increase this digit
    else:
        for digit in second_half:
            changes.append(9 - digit)  # Max we can increase this digit
    
    # Sort changes in descending order
    changes.sort(reverse=True)
    
    # Find minimum replacements
    replacements = 0
    for change in changes:
        diff -= change
        replacements += 1
        if diff <= 0:
            break
    
    return replacements

# Input
ticket = input().strip()
# Output
print(min_replacements_to_lucky(ticket))