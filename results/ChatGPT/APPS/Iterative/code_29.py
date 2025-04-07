def min_replacements(ticket):
    first_half = list(map(int, ticket[:3]))
    second_half = list(map(int, ticket[3:]))
    
    sum_first = sum(first_half)
    sum_second = sum(second_half)
    
    # If already lucky
    if sum_first == sum_second:
        return 0
    
    # Calculate the difference
    diff = abs(sum_first - sum_second)
    
    # Create lists of possible changes for each half
    if sum_first > sum_second:
        changes = sorted([9 - d for d in first_half], reverse=True)
    else:
        changes = sorted([9 - d for d in second_half], reverse=True)
    
    count = 0
    for change in changes:
        diff -= change
        count += 1
        if diff <= 0:
            return count
            
    return count

# Read input
ticket = input().strip()
# Get the result
result = min_replacements(ticket)
# Print the result
print(result)