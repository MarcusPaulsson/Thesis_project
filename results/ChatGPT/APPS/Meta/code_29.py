def min_replacements_to_lucky_ticket(ticket):
    # Split the ticket into two halves
    left = list(map(int, ticket[:3]))
    right = list(map(int, ticket[3:]))

    # Calculate the sums of the two halves
    left_sum = sum(left)
    right_sum = sum(right)

    # Calculate the difference
    diff = abs(left_sum - right_sum)
    
    # If the sums are already equal, no replacements are needed
    if diff == 0:
        return 0

    # Create a list of possible adjustments
    adjustments = []
    
    # Calculate the maximum possible adjustments from both halves
    for i in left:
        adjustments.append(9 - i)  # Max increase for left half
    for i in right:
        adjustments.append(i)        # Max decrease for right half

    # Sort adjustments in descending order
    adjustments.sort(reverse=True)

    # Initialize the number of replacements
    replacements = 0
    current_diff = 0

    # Make replacements until the current difference is covered
    for adjustment in adjustments:
        current_diff += adjustment
        replacements += 1
        if current_diff >= diff:
            break
    
    return replacements

# Example usage
ticket = input().strip()
print(min_replacements_to_lucky_ticket(ticket))