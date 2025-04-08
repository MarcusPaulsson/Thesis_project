def min_replacements_to_make_lucky(ticket: str) -> int:
    # Step 1: Split the ticket into two halves and convert to integers
    first_half = list(map(int, ticket[:3]))
    second_half = list(map(int, ticket[3:]))

    # Step 2: Calculate the sums of both halves
    sum_first = sum(first_half)
    sum_second = sum(second_half)

    # Step 3: If they are already equal, no replacements are needed
    if sum_first == sum_second:
        return 0

    # Step 4: Calculate the difference in sums
    difference = abs(sum_first - sum_second)

    # Step 5: Calculate potential changes for both halves
    changes = []
    if sum_first > sum_second:
        changes = sorted([digit for digit in second_half], reverse=True) + sorted([9 - digit for digit in first_half], reverse=True)
    else:
        changes = sorted([9 - digit for digit in first_half], reverse=True) + sorted([digit for digit in second_half], reverse=True)

    # Step 6: Count the minimum number of changes needed to cover the difference
    replacements = 0
    for change in changes:
        difference -= change
        replacements += 1
        if difference <= 0:
            break

    return replacements

# Example usage:
ticket = input().strip()
print(min_replacements_to_make_lucky(ticket))