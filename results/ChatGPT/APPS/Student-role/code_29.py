def min_replacements_to_lucky_ticket(ticket):
    first_half = list(map(int, ticket[:3]))
    second_half = list(map(int, ticket[3:]))
    
    sum_first = sum(first_half)
    sum_second = sum(second_half)
    
    if sum_first == sum_second:
        return 0
    
    diff = abs(sum_first - sum_second)
    
    # Create a list of possible changes
    changes = []
    
    if sum_first < sum_second:
        # We need to increase sum_first or decrease sum_second
        for digit in first_half:
            changes.append(9 - digit)  # max increase we can get
        for digit in second_half:
            changes.append(digit)       # max decrease we can get
    else:
        # We need to increase sum_second or decrease sum_first
        for digit in second_half:
            changes.append(9 - digit)  # max increase we can get
        for digit in first_half:
            changes.append(digit)       # max decrease we can get
    
    changes.sort(reverse=True)
    
    replacements = 0
    for change in changes:
        diff -= change
        replacements += 1
        if diff <= 0:
            break
            
    return replacements

# Read input
ticket = input().strip()
# Get the minimum replacements
result = min_replacements_to_lucky_ticket(ticket)
# Print the result
print(result)