def min_replacements_to_lucky_ticket(ticket):
    # Split the ticket into two halves
    first_half = list(map(int, ticket[:3]))
    second_half = list(map(int, ticket[3:]))

    # Calculate the sums of both halves
    sum_first = sum(first_half)
    sum_second = sum(second_half)

    # Calculate the difference
    difference = sum_first - sum_second
    # If the difference is zero, the ticket is already lucky
    if difference == 0:
        return 0

    # We need to make the sums equal, work with the absolute value of difference
    difference = abs(difference)

    # Create lists of potential changes for both halves
    first_half_changes = sorted([9 - digit for digit in first_half], reverse=True)
    second_half_changes = sorted([digit for digit in second_half], reverse=True)

    # Combine changes and sort them in descending order
    changes = sorted(first_half_changes + second_half_changes, reverse=True)

    # Calculate the minimum number of replacements needed
    replacements = 0
    for change in changes:
        difference -= change
        replacements += 1
        if difference <= 0:
            return replacements

    # If we exhaust all changes and still have a difference, it means we need more changes
    return replacements

# Input
ticket = input().strip()

# Output
print(min_replacements_to_lucky_ticket(ticket))