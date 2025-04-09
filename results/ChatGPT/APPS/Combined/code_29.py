def min_replacements_to_lucky_ticket(ticket: str) -> int:
    # Calculate the sums of the first and last three digits
    first_half_sum = sum(int(ticket[i]) for i in range(3))
    second_half_sum = sum(int(ticket[i]) for i in range(3, 6))
    
    # Calculate the difference between the two halves
    difference = abs(first_half_sum - second_half_sum)
    
    # If the ticket is already lucky
    if difference == 0:
        return 0
    
    # Get the maximum adjustments possible from each half
    first_half_adjustments = sorted(9 - int(ticket[i]) for i in range(3))
    second_half_adjustments = sorted(int(ticket[i]) for i in range(3, 6))
    
    # Combine adjustments and sort in descending order
    all_adjustments = sorted(first_half_adjustments + second_half_adjustments, reverse=True)
    
    # Try to minimize the number of replacements
    replacements = 0
    for adjustment in all_adjustments:
        difference -= adjustment
        replacements += 1
        if difference <= 0:
            return replacements
            
    return replacements  # In case we didn't reach zero

# Example usage
if __name__ == "__main__":
    ticket = input().strip()
    print(min_replacements_to_lucky_ticket(ticket))