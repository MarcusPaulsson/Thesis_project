def min_replacements_to_lucky(ticket):
    first_half = list(map(int, ticket[:3]))
    second_half = list(map(int, ticket[3:]))
    
    sum_first = sum(first_half)
    sum_second = sum(second_half)
    
    if sum_first == sum_second:
        return 0
    
    diff = abs(sum_first - sum_second)
    
    # Calculate the maximum possible changes we can make
    changes = []
    
    if sum_first > sum_second:
        # We need to reduce the first half or increase the second half
        changes = [9 - digit for digit in first_half] + second_half
    else:
        # We need to reduce the second half or increase the first half
        changes = first_half + [9 - digit for digit in second_half]
    
    # Sort changes in descending order
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
# Get the result and print it
print(min_replacements_to_lucky(ticket))