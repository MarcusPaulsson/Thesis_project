def min_replacements_to_lucky(ticket):
    first_half = list(map(int, ticket[:3]))
    second_half = list(map(int, ticket[3:]))
    
    sum_first = sum(first_half)
    sum_second = sum(second_half)
    
    if sum_first == sum_second:
        return 0
    
    diff = abs(sum_first - sum_second)
    
    # Calculate the maximum possible changes
    changes = []
    if sum_first > sum_second:
        changes = [9 - digit for digit in second_half]
    else:
        changes = [9 - digit for digit in first_half]
    
    changes.sort(reverse=True)
    
    count = 0
    for change in changes:
        diff -= change
        count += 1
        if diff <= 0:
            break
            
    return count

ticket = input().strip()
print(min_replacements_to_lucky(ticket))