def min_replacements_to_lucky_ticket(ticket):
    first_half = list(map(int, ticket[:3]))
    second_half = list(map(int, ticket[3:]))
    
    sum_first = sum(first_half)
    sum_second = sum(second_half)
    
    if sum_first == sum_second:
        return 0
    
    diff = abs(sum_first - sum_second)
    
    # Create a list of possible gains from changing each digit
    gains = []
    if sum_first > sum_second:
        for digit in first_half:
            gains.append(digit)  # Changing this digit to 0 will reduce the sum
        for digit in second_half:
            gains.append(9 - digit)  # Changing this digit to 9 will increase the sum
    else:
        for digit in second_half:
            gains.append(digit)  # Changing this digit to 0 will reduce the sum
        for digit in first_half:
            gains.append(9 - digit)  # Changing this digit to 9 will increase the sum
    
    # Sort gains in descending order to maximize the effect with the least changes
    gains.sort(reverse=True)
    
    count_replacements = 0
    for gain in gains:
        diff -= gain
        count_replacements += 1
        if diff <= 0:
            break
    
    return count_replacements

# Input
ticket = input().strip()
# Output
print(min_replacements_to_lucky_ticket(ticket))