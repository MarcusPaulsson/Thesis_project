def min_replacements_to_lucky(ticket):
    if len(ticket) != 6 or not ticket.isdigit():
        raise ValueError("Ticket must be a string of 6 digits.")

    first_half = list(map(int, ticket[:3]))
    second_half = list(map(int, ticket[3:]))
    
    sum_first = sum(first_half)
    sum_second = sum(second_half)
    
    if sum_first == sum_second:
        return 0
    
    diff = abs(sum_first - sum_second)
    
    # Calculate the maximum possible changes for each digit
    changes = [(9 - digit) if i < 3 else digit for i, digit in enumerate(first_half + second_half)]
    
    changes.sort(reverse=True)  # Sort changes in descending order
    
    count = 0
    for change in changes:
        diff -= change
        count += 1
        if diff <= 0:
            return count
    
    return count  # This will only happen if there are not enough digits to cover the difference


# Input reading
ticket = input().strip()
print(min_replacements_to_lucky(ticket))