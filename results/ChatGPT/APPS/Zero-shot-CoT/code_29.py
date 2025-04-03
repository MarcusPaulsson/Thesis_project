def min_replacements_to_lucky(ticket):
    first_half = ticket[:3]
    second_half = ticket[3:]

    sum_first = sum(int(digit) for digit in first_half)
    sum_second = sum(int(digit) for digit in second_half)

    if sum_first == sum_second:
        return 0

    # Calculate the differences
    diff = abs(sum_first - sum_second)

    # Create a list of possible changes (max changes per digit)
    changes = []
    if sum_first < sum_second:
        for digit in first_half:
            changes.append(9 - int(digit))  # Max possible gain from first half
    else:
        for digit in second_half:
            changes.append(9 - int(digit))  # Max possible gain from second half

    # Sort the changes in descending order
    changes.sort(reverse=True)

    # Count the minimum number of changes needed
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